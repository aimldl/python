#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pnlp-4_english-5_modeling_with_rnn.py
pnlp-4_text_classification-english_sentiment_analysis-5_modeling_with_rnn.py

Source: Python Natural Language Processing
Advanced machine learning and deep learning techniques for natural language processing
Jalaj Thanaki

파이썬 자연어 처리의 이론과 실제
효율적인 자연어 처리를 위한 머신 러닝과 딥러닝 구현하기
04. 텍스트분류 > 01. 영어 텍스트 분류
pp.146~212

* Dataset
IMDB Movie Review

Bag of Words Meets Bags of Popcorn
https://www.kaggle.com/c/word2vec-nlp-tutorial
"""

import os
import json

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.feature_extraction.text import CountVectorizer

import tensorflow as tf
#%%###################
data_in_path   = '../data_in/'
data_out_path  = '../data_out/'
checkpoint_rnn = '../checkpoint/rnn'

if not os.path.exists( data_out_path ):
    os.makerdirs( data_out_path )

# The input & label data were saved to a Numpy file.
train_input_data = 'train_input.npy'
train_label_data = 'train_label.npy'
test_input_data  = 'test_input.npy'
test_id_data     = 'test_id.npy'

data_configs     = 'data_configs.json'

#%%##############
# Load the data #
#################
# The preprocessed data was saved to numpy files (binary)
file = data_out_path + train_input_data
with open( file, 'rb') as f:
    input_data = np.load( f )
    print(f'Loaded from {file}...')

file = data_out_path + train_label_data
with open( file, 'rb') as f:
    label_data = np.load( f )
    print(f'Loaded from {file}...')

# The vocaburary and stuff...
prepro_configs = None
file = data_out_path + data_configs
with open( file, 'r') as f:
    prepro_configs = json.load( f )

#%%###############
# Configurations #
##################
random_seed      = 13371447
test_split_ratio = 0.1  # TODO:Why is this changed to 0.1 from 0.2?
batch_size       = 16
num_epochs       = 3

#%%###################
# Training the Model #
######################
# Split training and testing data
train_input, test_input, train_label, test_label = train_test_split( input_data, label_data, test_size=test_split_ratio, random_state=random_seed )
# train_input, eval_input, train_label, eval_label = train_input, test_input, train_label, test_label
# train_data_features, y = input_data, label_data

def mapping_fn(x, y):
    inputs, labels = {'x': x}, y
    return inputs, labels

def train_input_fn():
    dataset  = tf.data.Dataset.from_tensor_slices( (train_input, train_label) )
    dataset  = tf.data.shuffle( buffer_size=50000 )
    dataset  = tf.data.batch( batch_size )
    dataset  = tf.data.repeat( count=num_epochs )
    dataset  = tf.data.map( mapping_fn )
    iterator = dataset.make_one_shot_iterator()
    
    return iterator.get_next()

def eval_input_fn():
    dataset  = tf.data.Dataset.from_tensor_slices( (test_input, train_label) )
    dataset  = tf.data.batch( batch_size )
    dataset  = tf.data.map( mapping_fn )
    #dataset  = tf.data.batch( batch_size*2 )  # TODO: why *2  and AFTER map?
    iterator = dataset.make_one_shot_iterator()
    
    return iterator.get_next()

#%%###################
# Training the Model #
######################
print( type( prepro_configs['vocab_size'] ) )
# TypeError: string indices must be integers
print( prepro_configs['vocab_size'] )
vocab_size        = prepro_configs['vocab_size'] + 1  # +1 is for 'unk' or unknown
word_embeding_dim = 100
hidden_state_dim  = 150
dense_feature_dim = 150
drop_out_rate     = 0.2
learning_rate     = 0.001

# Double check the result
print( len(prepro_configs['vocab']), vocab_size )
# TODO: assert?

def model_fn( features, labels, mode ):
    # True if the condition is met
    training_mode   = ( mode == tf.estimator.ModeKeys.TRAIN )    
    testing_mode    = ( mode == tf.estimator.ModeKeys.EVAL )
    prediction_mode = ( mode == tf.estimator.ModeKeys.PREDICT )
    
    input_data      = features['x']
    embedding_layer = tf.keras.layers.Embedding( vocab_size, word_embeding_dim)( input_data )
    rnn_layers      = [tf.nn.rnn_cell.LSTMCell(size) for size in [hidden_state_dim, hidden_state_dim]]
    multi_rnn_cell  = tf.nn.rnn_cell.MultiRNNCell( rnn_layers )
    outputs, state  = tf.nn.dynamic_rnn( cell=multi_rnn_cell,
                                         inputs=embedding_layer,
                                         dtype=tf.float32 )
    
    outputs          = tf.keras.layers.Dropout( drop_out_rate )( outputs )
    hidden_layer     = tf.keras.layers.Dense( dense_feature_dim,
                                              activation=tf.nn.tanh )( outputs[:,-1,:] )
    hidden_layer     = tf.keras.layers.Dropout( drop_out_rate )( hidden_layer )
    
    logits           = tf.keras.layers.Dense(1)( hidden_layer )
    logits           = tf.squeeze( logits, axis=-1 )
    sigmoid_logits   = tf.nn.sigmoid( logits )
    
    # TODO: I have to double-check if logits are the right one to use!
    loss             = tf.losses.sigmoid_cross_entropy( labels, logits )
    
    if training_mode:
        global_step = tf.train.get_global_step()
        train_op    = tf.train.AdamOptimizer( learning_rate ).minimize( loss, global_step )
        
        return tf.estimator.EstimatorSpec( mode=mode, train_opt=train_op, loss=loss )
    
    if testing_mode:
        classes         = tf.round( sigmoid_logits)
        accuracy        = tf.metrics.accuracy( labels, classes )
        eval_metric_ops = {'acc': accuracy}  # TODO: or acc-> accuracy
        
        return tf.estimator.EstimatorSpec( mode=mode, loss=loss, eval_metric_ops = eval_metric_ops )
    
    if prediction_mode:
        predictions = {'sentiment': sigmoid_logits }
        
        return tf.estimator.EstimatorSpec( mode=mode, predictions=predictions )

#%%#################
# Train & Evaluate #
####################
os.environ['CUDA_VISIBLE_DEVICES']='4'

directory = data_out_path + checkpoint_rnn
est = tf.estimator.Estimator( model_fn=model_fn, model_dir=directory)
est.train( train_input_fn )
est.evaluate( eval_input_fn )

#%%##############
# Load the data #
#################
# The preprocessed data was saved to numpy files (binary)
file = data_out_path + test_input_data
with open( file, 'rb') as f:
    #te  st_input_data = np.load( f )
    print(f'Loaded from {file}...')

