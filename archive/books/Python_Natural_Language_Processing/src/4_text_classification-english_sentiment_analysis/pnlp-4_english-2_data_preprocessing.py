#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pnlp-4_english-2_data_preprocessing.py
pnlp-4_text_classification-english_sentiment_analysis-2_data_preprocessing.py

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

# ! pip install keras

#%%###################
# Data Preprocessing #
######################

import re
import numpy as np
import pandas as pd
import json

from bs4 import BeautifulSoup
from nltk.corpus import stopwords

from keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

data_in_path = '../data_in/'
labeld_train_data_tsv = 'labeledTrainData.tsv'

file = data_in_path + labeld_train_data_tsv
train_data = pd.read_csv( file, header=0, delimiter='\t', quoting=3 )

# The first review
print( train_data['review'][0] )
#"With all this stuff going down at the moment with MJ i've started listening to his music, watching the odd documentary here and there, watched The Wiz and watched Moonwalker again. Maybe i just want to get a certain insight into this guy who i thought was really cool in the eighties just to maybe make up my mind whether he is guilty or innocent. Moonwalker is part biography, part feature film which i remember going to see at the cinema when it was originally released. Some of it has subtle messages about MJ's feeling towards the press and also the obvious message of drugs are bad m'kay.<br /><br />Visually impressive but of course this is all about Michael Jackson so unless you remotely like MJ in anyway then you are going to hate this and find it boring. Some may call MJ an egotist for consenting to the making of this movie BUT MJ and most of his fans would say that he made it for the fans which if true is really nice of him.<br /><br />The actual feature film bit when it finally starts is only on for 20 minutes or so excluding the Smooth Criminal sequence and Joe Pesci is convincing as a psychopathic all powerful drug lord. Why he wants MJ dead so bad is beyond me. Because MJ overheard his plans? Nah, Joe Pesci's character ranted that he wanted people to know it is he who is supplying drugs etc so i dunno, maybe he just hates MJ's music.<br /><br />Lots of cool things in this like MJ turning into a car and a robot and the whole Speed Demon sequence. Also, the director must have had the patience of a saint when it came to filming the kiddy Bad sequence as usually directors hate working with one kid let alone a whole bunch of them performing a complex dance scene.<br /><br />Bottom line, this movie is for people who like MJ on one level or another (which i think is most people). If not, then stay away. It does try and give off a wholesome message and ironically MJ's bestest buddy in this movie is a girl! Michael Jackson is truly one of the most talented people ever to grace this planet but is he guilty? Well, with all the attention i've gave this subject....hmmm well i don't know because people can be different behind closed doors, i know this for a fact. He is either an extremely nice but stupid guy or one of the most sickest liars. I hope he is not the latter."

review = train_data['review'][0]

def preprocessing( review, remove_stopwords=True, remove_html_tags=True, verbose=False ):
    """
    ## Prerequisite
    NLTK's stop word list is used, so download it as follows:
        
    import nltk
    nltk.download('stopwords')
    """
    # Remove html tags
    if remove_html_tags:
        review = BeautifulSoup( review, 'html5lib').get_text()
    
    if verbose:
        print('-'*70)
        print( review )
        #"With all this stuff going down at the moment with MJ i've started listening to his music, watching the odd documentary here and there, watched The Wiz and watched Moonwalker again. Maybe i just want to get a certain insight into this guy who i thought was really cool in the eighties just to maybe make up my mind whether he is guilty or innocent. Moonwalker is part biography, part feature film which i remember going to see at the cinema when it was originally released. Some of it has subtle messages about MJ's feeling towards the press and also the obvious message of drugs are bad m'kay.Visually impressive but of course this is all about Michael Jackson so unless you remotely like MJ in anyway then you are going to hate this and find it boring. Some may call MJ an egotist for consenting to the making of this movie BUT MJ and most of his fans would say that he made it for the fans which if true is really nice of him.The actual feature film bit when it finally starts is only on for 20 minutes or so excluding the Smooth Criminal sequence and Joe Pesci is convincing as a psychopathic all powerful drug lord. Why he wants MJ dead so bad is beyond me. Because MJ overheard his plans? Nah, Joe Pesci's character ranted that he wanted people to know it is he who is supplying drugs etc so i dunno, maybe he just hates MJ's music.Lots of cool things in this like MJ turning into a car and a robot and the whole Speed Demon sequence. Also, the director must have had the patience of a saint when it came to filming the kiddy Bad sequence as usually directors hate working with one kid let alone a whole bunch of them performing a complex dance scene.Bottom line, this movie is for people who like MJ on one level or another (which i think is most people). If not, then stay away. It does try and give off a wholesome message and ironically MJ's bestest buddy in this movie is a girl! Michael Jackson is truly one of the most talented people ever to grace this planet but is he guilty? Well, with all the attention i've gave this subject....hmmm well i don't know because people can be different behind closed doors, i know this for a fact. He is either an extremely nice but stupid guy or one of the most sickest liars. I hope he is not the latter."
    
    # Substitute everything, but lower- & upper-case letters to space ' '
    review = re.sub('[^a-zA-Z]', ' ', review)
    
    if verbose:
        print('-'*70)
        print( review )
    
    # Convert all characters to the lower case & split into a list of words
    words  = review.lower().split()

    if verbose:
        print('-'*70)
        print( review )
    
    if remove_stopwords:
        stop_words = set( stopwords.words('english') )
        # Remove stop words
        words = [w for w in words if not w in stop_words]
    
    # Put the words together
    clean_review = ' '.join( words )    

    if verbose:
        print('-'*70)
        print( clean_review )

        vocalubrary = set( words )
        print('-'*70)
        print( vocalubrary )
        print('-'*70)
        print( words )
        print('-'*70)
        print( 'word/vocab ratio=', len(words)/len(vocalubrary) )   

    return clean_review
    
clean_train_reviews = []
for review in train_data['review']:
    clean_review = preprocessing( review )
    clean_train_reviews.append( clean_review )

print('-'*70)    
print( clean_train_reviews[0] )
print('-'*70)
print( clean_train_reviews[1] )

# TODO: put sentiment first!
# Create a data frame at this point
clean_train_df = pd.DataFrame( {'review': clean_train_reviews,
                                'sentiment': train_data['sentiment'] } )

# Tokenize the reviews
tokenizer = Tokenizer()
tokenizer.fit_on_texts( clean_train_reviews )

# Convert the tokens to indices
text_sequences = tokenizer.texts_to_sequences( clean_train_reviews )
print( text_sequences[0] )

word_vocab = tokenizer.word_index
print( word_vocab )
print( len(word_vocab) )  # 74065

# Save the vocaburary to a data frame.
data_configs = {}  # Dictionary
data_configs['vocab'] = word_vocab
data_configs['vocab_size'] = len( word_vocab) +1  # +1 is for <unk> unknown

# MAX_SEQUENCE_LENGTH is median of the word counts stats.
# Using average may be a bad idea. Some samples with too large words
# may dramatically increase the value of average. 
MAX_SEQUENCE_LENGTH = 174

# Use zero padding. Put zeros at the end of the remaining part of sentences.
train_intputs = pad_sequences( text_sequences,
                               maxlen=MAX_SEQUENCE_LENGTH,
                               padding='post' )
print( 'Shape of the training data:', train_intputs.shape )

# By doing this, all the 50k data has the same length.

# Save the labels as a numpy array.

train_labels = np.array( train_data['sentiment'] )
print('Shape of label tensor:', train_labels.shape)
# 25000,


# The preprocessed data will be saved to use during the modeling process.
# Four types of data are stored in the specified format.
#   clean text data         -> .csv file
#   vectorized data         -> Numpy file
#   label data              -> Numpy file
#   information on the data -> JSON file
# Information on the data is the vocabulary size and the total word count.

import os

data_out_path = '../data_out/'

if not os.path.exists( data_out_path ):
    os.makedirs( data_out_path )

train_clean_data = 'train_clean.csv'
train_input_data = 'train_input.npy'
train_label_data = 'train_label.npy'
data_configs     = 'data_configs.json'

# The preprocessed data was saved to a csv file
file       = data_out_path + train_clean_data
clean_train_df.to_csv( file, index=False )
print(f'Saved to {file}...')

# Save the preprocessed data to numpy files (binary)
with open(data_out_path + train_input_data, 'wb') as f:
    np.save( f, train_intputs )
    
with open( data_out_path + train_label_data, 'wb') as f:
    np.save( f, train_labels )

# The vocaburary and stuff...
with open( data_out_path + data_configs, 'w') as f:
    json.dump(data_configs, f, ensure_ascii=False)

#%%##############
# The test data #
#################

test_data_tsv = 'testData.tsv'
test_data = pd.read_csv( data_in_path + test_data_tsv, header=0, delimiter='\t', quoting=3 )

clean_test_reviews = []
for review in test_data['review']:
    clean_review = preprocessing( review )
    clean_test_reviews.append( clean_review )
clean_test_df = pd.DataFrame( {'review': clean_test_reviews, 'id': test_data['id'] } )
test_id = np.array( test_data['id'] )

# Note the tokenizer was not trained again!
# The same tokenizer as the training data must be used.
tokenizer.fit_on_texts( clean_test_reviews )
text_sequences = tokenizer.texts_to_sequences( clean_test_reviews )
# Use zero padding. Put zeros at the end of the remaining part of sentences.
test_intputs = pad_sequences( text_sequences,
                              maxlen=MAX_SEQUENCE_LENGTH,
                              padding='post' )

# TODO: Q: What about the out-of-vocabulary words?

test_clean_data = 'test_clean.csv'
test_input_data = 'test_input.npy'
test_id_data    = 'test_id.npy'

# The preprocessed data is saved to a csv file
clean_test_df.to_csv( data_out_path + test_clean_data, index=False )

# Save the preprocessed data to numpy files (binary)
with open(data_out_path + test_input_data, 'wb') as f:
    np.save( f, test_input_data )
    
with open( data_out_path + test_id_data, 'wb') as f:
    np.save( f, test_id_data )
