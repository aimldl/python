#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pnlp-4_english-6_modeling_with_cnn-refactored.py
pnlp-4_text_classification-english_sentiment_analysis-...

This is a refactorized version.
There're some minor changes in the variable names and so on.

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
import sys
import os
import json

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence

#%%##################
# Directory & Files #
#####################
dir_data_in        = '../data_in/'
dir_data_out       = '../data_out/'
#dir_checkpoint_rnn = '../checkpoint/rnn'

if not os.path.exists( dir_data_out ):
    os.makerdirs( dir_data_out )

# The input & label data were saved to a Numpy file.
file_train_input_data = 'train_input.npy'
file_train_label_data = 'train_label.npy'
file_test_input_data  = 'test_input.npy'
file_test_id_data     = 'test_id.npy'

file_data_configs     = 'data_configs.json'
#file_result_output    = 'movie_review_result-rnn.csv'

#%%######################
# Functions Definitions #
#########################

def save2np( file, mode='wb'):
    '''
    saves to a Numpy file.
        file  the full path to the file
          
    Usage:
        save2np( dir_data_out + file_test_input_data )
        or
        save2np( dir_data_out + file_test_input_data, 'wb' )
    '''
    with open( file, mode ) as f:
        np.save( f, file )
        print(f'Saved to {file}...')

def load_np( file, mode='rb'):
    '''
    loads from a Numpy file.
        file  the full path to the file
          
    Usage:
        train_input_data = load_np( dir_data_out + file_train_input_data )
        or
        train_input_data = load_np( dir_data_out + file_train_input_data, 'rb' )
    '''
    with open( file, mode ) as f:
        loaded_data = np.load( f )
        print(f'Loaded from {file}...')
        
    return loaded_data

def load_json( file, mode='r'):
    '''
    loads from a JSON file.
        file  the full path to the file
          
    Usage:
#        train_input_data = load_json( dir_data_out + file_train_input_data )
#        or
#        train_input_data = load_np( dir_data_out + file_train_input_data, 'rb' )
    '''
    with open( file, mode ) as f:
        loaded_data = json.load( f )
        print(f'Loaded from {file}...')
        
    return loaded_data

#%%##############
# Load the data #
#################
# The preprocessed data was saved to numpy files (binary)

train_input_data = load_np( dir_data_out + file_train_input_data )
train_label_data = load_np( dir_data_out + file_train_label_data )
test_input_data  = load_np( dir_data_out + file_test_input_data )

prepro_configs   = load_json( dir_data_out + file_data_configs )
print( prepro_configs.keys() )
