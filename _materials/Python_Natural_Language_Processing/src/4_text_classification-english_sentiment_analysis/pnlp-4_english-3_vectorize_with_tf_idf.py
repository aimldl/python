#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pnlp-4_english-3_vectorize_with_tf_idf.py
pnlp-4_text_classification-english_sentiment_analysis-3_vectorize_with_tf_idf.py

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

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#%%###################
data_out_path = '../data_out/'

if not os.path.exists( data_out_path ):
    os.makerdirs( data_out_path )

train_clean_data = 'train_clean.csv'
test_clean_data  = 'test_clean.csv'
lgs_tfids_answer = 'tfidf_logistic_regression_test_result.csv'

random_seed = 42
test_split_ratio = 0.2

# The preprocessed data was saved to a csv file
file       = data_out_path + train_clean_data
train_data = pd.read_csv( file, header=0, quoting=3 )
print(f'Read {file}...')

file       = data_out_path + test_clean_data
test_data  = pd.read_csv( file )
print(f'Read {file}...')

reviews    = train_data['review']
sentiments = train_data['sentiment']
#reviews    = list( train_data['review'] )
#sentiments = list( train_data['sentiment'] )

#print( reviews[1:2] )

#%%##########################
# Vectorization with TF-IDF #
#############################
# min_df minimum document frequency.
#vectorizer = TfidfVectorizer( min_df=0.0, analyzer='char', sublinear_tf=True, ngram_range(1,3), max_features=5000 )
vectorizer = TfidfVectorizer(min_df = 0.0, analyzer="char", sublinear_tf=True, ngram_range=(1,3), max_features=5000) 

# TODO: fix
#    vectorizer = TfidfVectorizer( min_df=0.0, analyzer='char', sublinear_tf=True, ngram_range(1,3), max_features=5000 )
#SyntaxError: positional argument follows keyword argument
x = vectorizer.fit_transform( reviews )
y = np.array( sentiments )

features = vectorizer.get_feature_names()

#%%##########################
# Vectorization with TF-IDF #
#############################
train_input, test_input, train_label, test_label = train_test_split( x, y, test_size=test_split_ratio, random_state=random_seed )
# x_train, x_eval, y_train, y_eval = train_input, test_input, train_label, test_label


lgs = LogisticRegression( class_weight='balanced' )
lgs.fit( train_input, train_label )

predicted = lgs.predict( test_input )
accuracy  = lgs.score( test_input, test_label )

print(f'accuracy = {accuracy}')
# accuracy = 0.8596

test_reviews   = test_data['review']  # Better to do list( test_data['review'] )?
test_data_feature_vect = vectorizer.transform( test_reviews )
prediction_result = lgs.predict( test_data_feature_vect )
print( prediction_result )
#[1 0 1 ... 0 1 0]

ids = test_data['id']  # Better to do list( test_data['id'] )?
answer_dataset = pd.DataFrame( {'id': ids , 'sentiment': prediction_result } )
file = data_out_path + lgs_tfids_answer
print(f'Saving to {file}...')
answer_dataset.to_csv( file , index=False, quoting=3)
