#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
text_encoding.py
# Sentiment Indentification for Roman Urdu
'''

import os
import sys

import numpy as np
import pandas as pd

from   tensorflow.keras.preprocessing.sequence import pad_sequences
from   collections import Counter
from   tensorflow.keras.preprocessing.text import Tokenizer
from   sklearn.feature_extraction.text import TfidfVectorizer
from   sklearn.feature_extraction.text import CountVectorizer

# Custom module
import functions4nlp
import functions4eda as eda

class TextEncoding:
    # Constructor
    def __init__(self):
        self.nlp = functions4nlp.NaturalLanguageProcessing()
	
    def test_keys( self, df_vocab, verbose=False, debug=False, dummy_input=False ):
        '''
        This function is created to test the keys in the vocabulary df_vocab
          because KeyError has occured in function encode_text_from.
              indexs = [ int( token2id_dict[ token ] ) for token in tokens ]
              KeyError: 'nan'
              
        Running this function reveals index=19850 has NaN.
            ipdb> df_vocab.loc[19850]
            id            19850
            vocabulary      NaN
            count             2
            Name: 19850, dtype: object
        
        I ran test_vocabulary_list in functions4nlp.py to test if 19850 is empty.
        It turned out that there's a vocabulary 'nan' in the vocabulary list.
        This complicates how to deal with 
        '''
        assert isinstance( df_vocab, pd.DataFrame), 'df_vocab must be a pandas.DataFrame.'

        print( 'Starting test_keys: vocalulary with NaN is displayed below.' )
        keys = df_vocab['vocabulary']
        for index, key in enumerate( keys, 0):
            if pd.isnull( key ):
                print( df_vocab.loc[index] )
        print( 'End of test_keys' )

    def filter_unknown_vocab_from( self, df_text, df_vocab, max_token_length, verbose=False, debug=False, dummy_input=False ):
        '''
        Note there're many duplicate reviews AFTER the preprocessing.
        These duplicates should be removed.
          df_text['review'].shape
          (19128,)
          df_text['review'].drop_duplicates().shape
          (18841,)
          df_text['review'].unique().shape
          (18841,)
           
        drop_duplicates() returns a Series while unique() returns a Numpy array.
        
         A valid vocabulary 'nan' causes "KeyError: 'nan'"
           because it's recognized as NaN (Not a number).
         As a quick fix, the vocabulary 'nan' is removed in other script
           because it has only two counts.
         TODO: This is a quick fix. Watch out for this in the later part.

        '''
        assert isinstance( df_text, pd.DataFrame), 'df_text must be a pandas.DataFrame.'
        assert isinstance( df_vocab, pd.DataFrame), 'df_vocab must be a pandas.DataFrame.'
        print( "Filtering unknown vocabularies from 'df_text' with reference to a dictionary 'df_vocab'..." )

        #verbose = True
        token2id_dict = dict( zip( df_vocab['vocabulary'], df_vocab['id'] ) )
        documents_list   = list( df_text['review'] )
        labels_list      = list( df_text['sentiment'] )

        filtered_documents_list = []
        filtered_labels_list    = []
        for index, document in enumerate( documents_list, 0 ):
            tokens = self.nlp.tokenize( document )
            if verbose:
                print( tokens )

            filtered_tokens = []
            token_count = 0
            for token in tokens:  # this token is key of a dictionary
                # If token doesn't exist in the dictionary, it's [unk]
                # vocabulary with low frequency is removed from the vocabulary dictionary. 
                value = token2id_dict.get( token )
                
                if value:              # If found,
                    filtered_tokens.append( token )
                else:                  # If not found,
                    filtered_tokens.append( '[unk]' )
                    
                token_count += 1
            # Filter out a document longer than max_token_count
            if verbose:
                print( index, labels_list[index] )
                print( token_count, document )

            if token_count < max_token_length:
                recreated_document = ' '.join( filtered_tokens )
                filtered_documents_list.append( recreated_document )
                filtered_labels_list.append( labels_list[index] )

        # 1787 reviews are filtered compared to the original review.
        df = pd.DataFrame( filtered_documents_list, columns=['review'] )
        df.insert(0, 'sentiment', filtered_labels_list, False )

        # There're 839 duplicates which are also removed.
        file_duplicated = '../output/df_duplicated.csv'
        df_duplicated = df[ df.duplicated( subset=['review'] ) ]
        df_duplicated = df_duplicated.sort_values( by=['review','sentiment'])
        df_duplicated.to_csv( file_duplicated )
        print('Saved to', file_duplicated)

        # Duplicates in 'review' are removed along with the corresponding 'sentiment'.
        # Note the last one is kept because, at least, one should remain.
        df = df.drop_duplicates( subset=['review'], keep="last" )
        df = df.sort_values( by=['review','sentiment'])
        df.index.name = 'index'
        df_filtered_documents = df

        return df_filtered_documents
	
    def encode_text_from( self, df_text, df_vocab, max_token_length, verbose=False, debug=False, dummy_input=False ):
        assert isinstance( df_text, pd.DataFrame), 'df_text must be a pandas.DataFrame.'
        assert isinstance( df_vocab, pd.DataFrame), 'df_vocab must be a pandas.DataFrame.'
        print( "Encoding the text input 'df_text' with reference to a dictionary 'df_vocab'..." )

        #debug = True   
        token2id_dict = dict( zip( df_vocab['vocabulary'], df_vocab['id'] ) )
        documents_list   = list( df_text['review'] )

        oov_count = 0  # Out-of-Vocabulary
        documents_in_id_list  = []
        oov_token_list        = []
        for index, document in enumerate( documents_list, 0 ):
            tokens = self.nlp.tokenize( document )
            if verbose:
                print( tokens )
            
            token_ids_list = []
            token_count = 0
            for token in tokens:  # this token is key of a dictionary
                token_id = token2id_dict.get( token )
                
                if token_id:              # If there exists an ID
                # I assume all the unknown tokens are converted to [unk],
                # so all the tokens should visit if.
                    token_ids_list.append( token_id )
                else:                  # If not found,
                    # This is for a fail-safe code
                    # The tokens mapped to [unk] as well as OOV are [unk].
                    if verbose:
                        print( f'Unknown vocabulary {token}' )
                    oov_token_list.append( token )
                    oov_count += 1
                    
                    token_id = 0  # [unk] is the ID for an unknown or OOV token
                    token_ids_list.append( token_id )
                    # TODO: Append the index for the document. Note: don't just save index. 
                    #       The 'shuffled' index from the dataframe must be saved.
                    
                token_count += 1  # For total number of tokens for this document
            
            documents_in_id_list.append( token_ids_list )
            # Make sure each index is an integer with int( . )
            #   which may not be neccessary, but just in case!
            if verbose:
                print( 'doc:', document )
                print( 'IDs:', token_ids_list )
            
        if verbose:
            print( documents_in_id_list )
        
        # Zero padding.
        #   Sequences that are shorter than max_sequence_length are padded with zeros at the end.
        #   Refer to https://keras.io/preprocessing/sequence/
        #        	https://www.tensorflow.org/beta/guide/keras/masking_and_padding
        encoded_documents_list = pad_sequences( documents_in_id_list, maxlen=max_token_length, padding='post' )
        if verbose:
            print('-'*40)
            print( encoded_documents_list )
            print('-'*40)


        df_encoded_documents = pd.DataFrame( encoded_documents_list )
        # CAUTION: If 'index' is used as the column name, the index of the new dataframe is missed up.
        #          Some values in 'index' are missing from drop_duplicates, but these values cause problems.
        df_index             = pd.DataFrame( list( df_text.index ), columns=['old_index'] )
        df_sentiment         = df_text['sentiment']
        assert ( df_index.shape[0]     == df_encoded_documents.shape[0] ), 'Error: The number of rows in both dataframes must be the same.'
        assert ( df_sentiment.shape[0] == df_encoded_documents.shape[0] ), 'Error: The number of rows in both dataframes must be the same.'
        
        df_encoded_text = pd.concat( [df_index, df_sentiment, df_encoded_documents], axis=1 )
        print( df_encoded_text.shape )
        #       index sentiment  0  1  2  3  4  5  6
        #	0     0         2    3  6  5  0  0  0  0
        #	1     2         1    6  2  5  4  0  0  0
        #	2     3         0    5  4  1  6  0  0  0
        #	3     4         2    6  3  4  0  0  0  0
        #	4     5         1    6  2  4  0  0  0  0
        #	5     7         0    1  6  0  0  0  0  0
        #	6     8         1    6  2  0  0  0  0  0
        #	7    10         1    6  5  4  0  0  0  0

        # Save oov_token_list as well as the document number (shuffled Index).
        # This is helpful to keep track of oov_tokens.
        # The list of unknown tokens must be saved in order to compare the saved oov_token_list.
        # Analysis to find oov tokens by comparing to the unknown list is necessary.
        # It'll help add more vocabulary.
            
        return df_encoded_text
        
	# texts2sequences (for a list input) is the precursor of encode_text_from (for a dataframe input).
	# I keep this function just in case.
    def texts2sequences( self, documents, token2index, verbose=False ):
        '''
        This is my custom texts_to_sequences like 
          from tensorflow.keras.preprocessing.text import Tokenizer
          tokenizer = Tokenizer()
          text_sequences = tokenizer.texts_to_sequences( clean_train_reviews )
        
        Usage:
             documents_in_id_list = texts2sequences( documents_list, token2id_dict )
        Example:
             input
               documents_list         = ['aa aa bb bb cc', 'aa cc dd', 'aa ee bb']
               token2id_dict       = {'dd': 1, 'cc': 2, 'bb': 3, 'aa': 4, 'ee': 5}

             output
               documents_in_id_list = [[4, 4, 3, 3, 2], [4, 2, 1], [4, 5, 3]]
        How it works:
             indexs = [ token2index[ token ] for token in tokens ]
               returns indexs of tokens and make it a list
             documents         = ['aa aa bb bb cc', 'aa cc dd', 'aa ee bb']
             document -> indexs  aa aa bb bb cc -> [4, 4, 3, 3, 2]
                                 aa cc dd -> [4, 2, 1]
                                 aa ee bb -> [4, 5, 3]
             indexed_documents = [[4, 4, 3, 3, 2], [4, 2, 1], [4, 5, 3]]
        '''
        assert isinstance( documents, list), 'documents must be a list'
        assert isinstance( token2index, dict), 'token2index must be a dictionary'
        
        indexed_documents = []
        for document in documents:
            tokens = self.tokenize( document )
            indexs = [ int( token2index[ token ] ) for token in tokens ]
            # Make sure each index is an integer with int( . )
            #   which may not be neccessary, but just in case!
            if verbose:
                print( document )
                print( indexs )
            indexed_documents.append( indexs )
        if verbose:
            print( indexed_documents )
        	
        return indexed_documents

        
#    def encode_text_from( self, df_text, df_vocab, verbose=False, debug=False, dummy_input=False ):
#        assert isinstance( df_text, pd.DataFrame), 'df_text must be a pandas.DataFrame.'
#        assert isinstance( df_vocab, pd.DataFrame), 'df_vocab must be a pandas.DataFrame.'
#        
#        print( "Encoding the text input 'df_text' with reference to a dictionary 'df_vocab'..." )	
#
#        labels = ['num_of_tokens', 'Frequency']  # per_review
#        median, upper_bound = eda.compute_stat_dispersion( num_of_tokens_list, labels[0] )
#        eda.plot_histogram( num_of_tokens_list, bins=200, yscale='linear', xlim=[1,100], xlabel=labels[0], ylabel=labels[1] )
#        eda.plot_histogram( num_of_tokens_list, bins=200, xlabel=labels[0], ylabel=labels[1] )
#
#        labels = ['tokens_count', 'Frequency']  # as a whole
#        tokens_count_list = list( df_vocab['count'] )
#        eda.compute_stat_dispersion( tokens_count_list, labels[0] )
#        eda.plot_histogram( tokens_count_list, bins=10000, yscale='linear', xlabel=labels[0], ylabel=labels[1], xlim=[1,35] )
#        eda.plot_histogram( tokens_count_list, bins=200, xlabel=labels[0], ylabel=labels[1], xlim=[1,1000] )
#
#        # max_sequence_length is median of the word counts stats.
#        # Using average may be a bad idea. Some samples with too large words
#        # may dramatically increase the value of average. 
#        max_sequence_length = int( median )
#
#        return df_vocab, vocab_size, max_sequence_length
# EOF