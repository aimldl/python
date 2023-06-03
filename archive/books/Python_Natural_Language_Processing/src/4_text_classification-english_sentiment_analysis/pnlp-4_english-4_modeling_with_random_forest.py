#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pnlp-4_english-4_modeling_with_random_forest.py
pnlp-4_text_classification-english_sentiment_analysis-4_modeling_with_random_forest.py

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

import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#%%###################
data_in_path = '../data_in/'
data_out_path = '../data_out/'

if not os.path.exists( data_out_path ):
    os.makerdirs( data_out_path )

train_clean_data = 'train_clean.csv'
test_clean_data  = 'test_clean.csv'

random_seed      = 42
test_split_ratio = 0.2

#%%##############
# Load the data #
#################
# The preprocessed data was saved to a csv file
file = data_out_path + train_clean_data
train_data = pd.read_csv( file )
print(f'Read {file}...')

file = data_out_path + test_clean_data
print(f'Reading in {file}...')
test_data  = pd.read_csv( file )

reviews    = list( train_data['review'] )
sentiments = list( train_data['sentiment'] )

y = np.array( sentiments )

#%%#################################
# Vectorizing with CountVectorizer #
####################################
vectorizer          = CountVectorizer( analyzer = 'word', max_features=5000 )
train_data_features = vectorizer.fit_transform( reviews )  # x = train_data_features

#%%###################
# Training the Model #
######################
# Split training and testing data
train_input, test_input, train_label, test_label = train_test_split( train_data_features, y, test_size=test_split_ratio, random_state=random_seed )
# x_train, x_eval, y_train, y_eval = train_input, eval_input, train_label, eval_label
# train_input, eval_input, train_label, eval_label = train_input, test_input, train_label, test_label

# Modeling with Random Forest
forest = RandomForestClassifier( n_estimators=100 )
forest.fit( train_input, train_label )

#predicted = lgs.predict( x_eval )
accuracy  = forest.score( test_input, test_label )

print(f'accuracy = {accuracy}')
# accuracy = 0.8596

#%%##################
# Testing the Model #
#####################
test_reviews = test_data['review']  # Better to do list( test_data['review'] )?
ids          = test_data['id']  # Better to do list( test_data['id'] )?

test_data_feature_vect = vectorizer.transform( test_reviews )
prediction_result = forest.predict( test_data_feature_vect )
print( prediction_result )

ids = test_data['id']  # Better to do list( test_data['id'] )?

#%%##################
# Saving the Result #
#####################

prediction_result_df = pd.DataFrame( {'id': ids , 'sentiment': prediction_result } )

random_forest_prediction_result_csv = 'bag_of_words_model.csv'
file = data_out_path + random_forest_prediction_result_csv
prediction_result_df.to_csv( file , index=False, quoting=3)
print(f'Saved to {file}...')
