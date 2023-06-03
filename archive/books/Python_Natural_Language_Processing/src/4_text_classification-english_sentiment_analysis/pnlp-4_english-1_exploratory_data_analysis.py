#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pnlp-4_english-1_exploratory_data_analysis.py
pnlp-4_text_classification-english_sentiment_analysis-1_exploratory_data_analysis.py

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

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

DATA_IN_PATH = '../data_in/'
file_list = ['labeledTrainData.tsv','testData.tsv', 'unlabeledTrainData.tsv']

train_data = pd.read_csv( DATA_IN_PATH + 'labeledTrainData.tsv', header=0, delimiter='\t', quoting=3 )

print( train_data.head() )
#         id  sentiment                                             review
#0  "5814_8"          1  "With all this stuff going down at the moment ...
#1  "2381_9"          1  "\"The Classic War of the Worlds\" by Timothy ...
#2  "7759_3"          0  "The film starts with a manager (Nicholas Bell...
#3  "3630_4"          0  "It must be assumed that those who praised thi...
#4  "9495_8"          1  "Superbly trashy and wondrously unpretentious ...

print('File size')
for file in os.listdir(DATA_IN_PATH):
    if 'tsv' in file and 'zip' not in file:
        file_size_in_MB = str( round( os.path.getsize( DATA_IN_PATH + file ) / 1000000, 2 ) )
        print( file.ljust(30) + file_size_in_MB + 'MB')
#        File size
#        labeledTrainData.tsv          33.56MB
#        testData.tsv                  32.72MB
#        unlabeledTrainData.tsv        67.28MB

train_data_size = len( train_data )
print( f'Training data size: {train_data_size}')
# Training data size: 25000

review_length = train_data['review'].apply(len)  # train_length
print( review_length.head() )
#0    2304
#1     948
#2    2451
#3    2247
#4    2233
#Name: review, dtype: int64

plt.figure( figsize=(12,5) )

plt.hist( review_length, bins=200, alpha=0.5, color='r', label='word' )
plt.yscale('log', nonposy='clip')

plt.title('Log-Histogram: Length of Review')
plt.xlabel('Length of Review')
plt.xlabel('Number of Review')

review_length_max        = np.max( review_length )
review_length_min        = np.min( review_length )
review_length_mean       = np.mean( review_length )
review_length_std        = np.std( review_length )
review_length_median     = np.median( review_length )
review_length_25_percent = np.percentile( review_length, 25 )
review_length_75_percent = np.percentile( review_length, 75 )

print(f'review_length_max: {review_length_max}')
print(f'review_length_min: {review_length_min}')
print(f'review_length_mean: {review_length_mean}')
print(f'review_length_std: {review_length_std}')
print(f'review_length_median: {review_length_median}')
print(f'review_length_25_percent: {review_length_25_percent}')
print(f'review_length_75_percent: {review_length_75_percent}')


def print_stats( data, name ):
    """
    name is a string
    Usage:
        print_stats(review_length,'review_length')
    """
    data_max        = np.max( data )
    data_min        = np.min( data )
    data_mean       = np.mean( data )
    data_std        = np.std( data )
    data_median     = np.median( data )
    data_25_percent = np.percentile( data, 25 )
    data_75_percent = np.percentile( data, 75 )
    
    print(f'{name}_max: {data_max}')
    print(f'{name}_min: {data_min}')
    print(f'{name}_mean: {data_mean}')
    print(f'{name}_std: {data_std}')
    print(f'{name}_median: {data_median}')
    print(f'{name}_25_percent: {data_25_percent}')
    print(f'{name}_75_percent: {data_75_percent}')

print('-'*70)

print_stats(review_length,'review_length')
print('-'*70)

plt.figure( figsize=(12,5) )

plt.boxplot( review_length, labels=['counts'], showmeans=True )

# ! pip install wordcloud
from wordcloud import WordCloud

cloud = WordCloud( width=800, height=600).generate(" ".join( train_data['review'] ))
plt.figure( figsize=(20,15) )
plt.imshow( cloud )
plt.axis('off')

# br is very large in the word cloud.
# So remove HTML tags

# Use Seaborn to plot the distribution of labels
fig, axe = plt.subplots( ncols=1 )
fig.set_size_inches( 6,3 )
sns.countplot( train_data['sentiment'] )

positive_reviews = train_data['sentiment'].value_counts()[1]
negative_reviews = train_data['sentiment'].value_counts()[0]

print(f'Positive reviews: {positive_reviews}')
print(f'Negative reviews: {negative_reviews}')

# Apply the lambda function for each entry of 'review' in the training data
#   lambda x: len( x.split(' ')

# TODO: train_word_counts --> token size or something.
train_word_counts = train_data['review'].apply( lambda x: len( x.split(' ') ))

plt.figure( figsize=(15,10) )
plt.hist( train_word_counts, bins=50, facecolor='r', label='train')
plt.title('Log-Histogram: Word Count in Review', fontsize=15 )
plt.yscale('log', nonposy='clip')
plt.legend()
plt.xlabel('Number of Words', fontsize=15 )
plt.ylabel('Number of Reviews', fontsize=15 )

print_stats(train_word_counts,'train_word_counts')

# Ratio of punctuations and characters (both lower and upper cases)


count_question_marks   = train_data['review'].apply( lambda x: '?' in x )
count_punctuations     = train_data['review'].apply( lambda x: '.' in x )
count_capitalized      = train_data['review'].apply( lambda x: x[0].isupper() )
count_upper_case_chars = train_data['review'].apply( lambda x: max( [y.isupper() for y in x]) )
count_numbers          = train_data['review'].apply( lambda x: max( [y.isdigit() for y in x]) )

mean_count_question_marks   = np.mean( count_question_marks )
mean_count_punctuations     = np.mean( count_punctuations )
mean_count_capitalized      = np.mean( count_capitalized )
mean_count_upper_case_chars = np.mean( count_upper_case_chars )
mean_count_numbers          = np.mean( count_numbers )

print('review with questionmarks: {.2f}%'.format( mean_count_question_marks* 100))
print('review with punctuations: {.2f}%'.format( mean_count_punctuations* 100))
print('review that is capitalized: {.2f}%'.format( mean_count_capitalized* 100))
print('review with upper case chars: {.2f}%'.format( mean_count_upper_case_chars* 100))
print('review with numbers: {.2f}%'.format( mean_count_numbers* 100))

# TODO: emoticons, hashtag, etc.
