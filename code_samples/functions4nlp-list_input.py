#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import math

import numpy as np
import pandas as pd
import regex

from   collections import Counter
from   tensorflow.keras.preprocessing.text import Tokenizer
from   sklearn.feature_extraction.text import TfidfVectorizer
from   sklearn.feature_extraction.text import CountVectorizer

# Custom module
import functions4eda as eda

class NaturalLanguageProcessing:
    # Constructor
    def __init__(self):
        self.vocabulary_set      = ()  # An empty set
        self.vocabulary_size     = -1
        self.token_count_median = -1 
        self.upper_bound         = -1 

#%%
    def analyze( self, documents_list, verbose=False ):
        '''
        Each row of a data frame or each review corresponds to a document.
        documents_list is a list of documents which is equal to:
            a column of a DataFrame or a Series converted to list or
            a list of reviews in movie reviews for a sentiment analysis task.
        Usage:
            list_indexed, max_sequence_length, data_configs_df \
              = self.nlp.analyze( list_preprocessed )
            
            Note: list_indexed is a list of lists.
        Example:
             input
                          documents_list: ['aa aa bb bb cc', 'aa cc dd', 'aa ee bb']
             output

        How it works:
       
        '''
        assert isinstance( documents_list, list), 'documents_list must be a list'
        if verbose:
            print( 'Analyzing documents_list ...' )

        tokenized_documents_list, num_of_tokens_list, vocabulary_list, token2index_dict \
          = self.analyze_documents( documents_list, verbose )
        
        # Save the vocaburary to a data frame.
        data_configs = {}  # An empty Dictionary
        data_configs['vocab'] = pd.Series( vocabulary_list )
        data_configs['vocab_size'] = len( vocabulary_list) +1  # +1 is for <unk> or unknown
        
        # Compute token_count_median to determine how many zero padding to use
        self.upper_bound        = eda.get_upper_bound( num_of_tokens_list )
        self.token_count_median = eda.get_median( num_of_tokens_list )
        #max_sequence_length     = self.token_count_median
        # max_sequence_length is median of the word counts stats.
        # Using average may be a bad idea. Some samples with too large words
        # may dramatically increase the value of average. 
        
        # OPTION
        #max_sequence_length     = math.ceil( self.token_count_median )
        #max_sequence_length     = math.ceil( self.upper_bound )
        max_sequence_length     = math.floor( self.upper_bound )
        assert isinstance( max_sequence_length, int ), 'isinstance must be an integer'
        # If max_sequence_length is a floating number, this will eventually cause an error by 
        #   list_indexed_and_padded = pad_sequences( list_indexed_np_array, maxlen=max_sequence_length, padding='post' )
        #   TypeError: 'numpy.float64' object cannot be interpreted as an integer
        #   maxlen only takes an integer!

        #documents = ['this is just a test of a document','hey this is another example of document','the last example is here']
        truncated_vocabulary_list, truncated_vocabulary_size \
          = self.get_truncated_vocaburary( documents_list, max_sequence_length)

#        if verbose:
        eda.print_stat_dispersion( num_of_tokens_list, 'num_of_tokens_list')
        print( 'token_count_median=', self.token_count_median )
        print( 'upper_bound=', self.upper_bound )
        print( 'max_sequence_length=', max_sequence_length )
        
        eda.plot_histogram( num_of_tokens_list, bins=200, yscale='linear', xlim=[1,100] )
        eda.plot_histogram( num_of_tokens_list, bins=200 )

        indexed_documents_list = self.texts2sequences( documents_list, token2index_dict )

        return indexed_documents_list, max_sequence_length, data_configs

    def analyze_documents( self, documents, verbose=False ):
        '''
        Usage:
             tokenized_documents_list, num_of_tokens_list, vocabulary_list, token2index_dict 
               = self.analyze_documents( documents_list, verbose )
        Example:
             input
                          documents_list: ['aa aa bb bb cc', 'aa cc dd', 'aa ee bb']
             output
                tokenized_documents_list: ['aa', 'aa', 'bb', 'bb', 'cc', 'aa', 'cc', 'dd', 'aa', 'ee', 'bb']
                      num_of_tokens_list: [5, 3, 3]
                         vocabulary_list: ['bb', 'cc', 'ee', 'aa', 'dd']
                        token2index_dict: {'bb': 1, 'cc': 2, 'ee': 3, 'aa': 4, 'dd': 5}
        How it works:
            This function calculates in the following order.
            
            documents -> tokenized_documents, num_of_tokens
                         tokenized_documents -> vocabulary
                                                vocabulary -> token2index
                         tokenized_documents -> tokens_count -> most_common_tokens
        Verbose output:
            document: aa aa bb bb cc
            tokens  : ['aa', 'aa', 'bb', 'bb', 'cc']
            document: aa cc dd
            tokens  : ['aa', 'cc', 'dd']
            document: aa ee bb
            tokens  : ['aa', 'ee', 'bb']
            tokenized_documents: ['aa', 'aa', 'bb', 'bb', 'cc', 'aa', 'cc', 'dd', 'aa', 'ee', 'bb']
                  num_of_tokens: [5, 3, 3]
                     vocabulary: ['bb', 'cc', 'ee', 'aa', 'dd']
                vocabulary_size: 6
                    token2index: {'bb': 1, 'cc': 2, 'ee': 3, 'aa': 4, 'dd': 5}
                   tokens_count: Counter({'aa': 4, 'bb': 3, 'cc': 2, 'dd': 1, 'ee': 1})
             most_common_tokens: [('aa', 4), ('bb', 3), ('cc', 2), ('dd', 1), ('ee', 1)]
        '''
        assert isinstance( documents, list), 'documents must be a list'

        # Compute 'tokenized_documents' & 'num_of_tokens'
        tokenized_documents = []  # This is an empty list
        num_of_tokens       = []  # This is an empty list
        for document in documents:
            # Make a list of tokenized_documents
            #   tokens is a list of tokens for a document
            #   num_of_tokens is the number of tokens in a document
            tokens       = self.tokenize( document )
            tokenized_documents.extend( tokens )
            num_of_tokens.append( len( tokens ) )

            if verbose:
                print( f'document: {document}' )
                print( f'tokens  : {tokens}' )

        # Compute 'vocabulary' from 'tokenized_documents'
        #   Convert the set to a list so vocabulary is easily accesible with index.
        vocabulary_set  = set( tokenized_documents )
        vocabulary      = list( vocabulary_set )  
        vocabulary_size = len( vocabulary )

        # Compute 'token2index' from 'vocabulary'
        #   Convert the tokens to indices
        #   Create a dictionry of tokens in the vocabulary mapped to index positions
        token2index = {}  # This is an empty dictionary
        # Note index starts from 1. 0 is reserved for [unk]
        for index, token in enumerate( vocabulary, 1 ):
            token2index[ token ] = index

        # Compute 'tokens_count' from 'tokenized_documents'
        # Just to see tokens_count.most_common()
        tokens_count       = Counter( tokenized_documents )
        most_common_tokens = tokens_count.most_common()
        
        if verbose:
            print( f'tokenized_documents: {tokenized_documents}')
            print( f'      num_of_tokens: {num_of_tokens}')
            print( f'         vocabulary: { vocabulary}' )
            print( f'        token2index: {token2index}' )
            print( f'       tokens_count: {tokens_count}' )
            print( f' most_common_tokens: {most_common_tokens}' )

        print( f'    vocabulary_size: { vocabulary_size}' )

        return tokenized_documents, num_of_tokens, vocabulary, token2index

    def tokenize( self, document_str):
        '''
        Should I go for a custom word tokenizer like NLTK's RegexpTokinizer?
        If so, the regular expression is. \w+\$[\d\.]+|\S+
        
        p = regex.compile( '\w+\$[\d\.]+|\S+' )
        df['token'] = df['review'].apply( lambda x: p.match(x).group() )
        '''
        assert isinstance(document_str, str), 'document_str must be a string'

        # A simple tokenizer with split because the document is clean.
        tokens = document_str.split(' ')
        return tokens

    def texts2sequences( self, documents, token2index, verbose=False ):
        '''
        This is my custom texts_to_sequences like 
          from tensorflow.keras.preprocessing.text import Tokenizer
          tokenizer = Tokenizer()
          text_sequences = tokenizer.texts_to_sequences( clean_train_reviews )
        
        Usage:
             indexed_documents_list = texts2sequences( documents_list, token2index_dict )
        Example:
             input
               documents_list         = ['aa aa bb bb cc', 'aa cc dd', 'aa ee bb']
               token2index_dict       = {'dd': 1, 'cc': 2, 'bb': 3, 'aa': 4, 'ee': 5}

             output
               indexed_documents_list = [[4, 4, 3, 3, 2], [4, 2, 1], [4, 5, 3]]
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

    def count_words(self, documents_list, verbose=False, normalized=True ):
        assert isinstance( documents_list, list), 'documents_list must be a list'
        '''
        Count how many times each unique word occurs in text.
        '''
        # print(documents_list)
        word_counts_dict = dict()  # dictionary of { <word>: <count> } pairs to return
        print(word_counts_dict)
        
#        for document in documents_list:
            
        if not normalized:
            # Convert to lowercase.
            # Normalization includes removing non-alphanumeric characters, too.
            # But it's done in other part, so I'll skip the task.
            documents_list = documents_list.lower()
            print( documents_list)
    
        # Split text into tokens (words), leaving out punctuation
        # Regex is used to split on non-alphanumeric characters.
        # remove special characters/whitespaces
        tokens = regex.split('[^a-zA-Z\s]', documents_list, regex.I|regex.A)
        print(tokens)
        
        # Aggregate word counts using a dictionary
        word_counts_dict = Counter(tokens)    
        print('-'*40)
        print( word_counts_dict )
        
        return word_counts_dict
#%%
    def get_truncated_vocaburary( self, documents, max_sequence_length, verbose=False ):
        '''
        Usage:
             vocabulary, vocabulary_size = nlp.get_truncated_vocaburary( documents, 5)
        Example:
            documents = ['this is just a test of a document','hey this is another example of document','the last example is here']
            vocabulary, vocabulary_size = nlp.get_truncated_vocaburary( documents, 5)
            0 this
            1 is
            2 just
            3 a
            4 test
            5 of
            tokenized_documents: ['this', 'is', 'just', 'a', 'test']
            truncated_document  : ['this', 'is', 'just', 'a', 'test']
            0 hey
            1 this
            2 is
            3 another
            4 example
            5 of
            tokenized_documents: ['this', 'is', 'just', 'a', 'test', 'hey', 'this', 'is', 'another', 'example']
            truncated_document  : ['hey', 'this', 'is', 'another', 'example']
            0 the
            1 last
            2 example
            3 is
            4 here
            tokenized_documents: ['this', 'is', 'just', 'a', 'test', 'hey', 'this', 'is', 'another', 'example', 'the', 'last', 'example', 'is', 'here']
            truncated_document  : ['the', 'last', 'example', 'is', 'here']
            tokenized_documents: ['this', 'is', 'just', 'a', 'test', 'hey', 'this', 'is', 'another', 'example', 'the', 'last', 'example', 'is', 'here']
                     vocabulary: ['another', 'the', 'example', 'is', 'test', 'a', 'just', 'hey', 'this', 'here', 'last']
                vocabulary_size: 11
        '''
        assert isinstance( documents, list), 'documents must be a list'
        assert isinstance( max_sequence_length, int), 'max_sequence_length must be an integer'

        # Compute 'tokenized_documents' & 'num_of_tokens'
        tokenized_documents = []  # This is an empty list
        num_of_tokens       = []  # This is an empty list
        for document in documents:
            # Make a list of tokenized_documents
            #   tokens is a list of tokens for a document
            #   num_of_tokens is the number of tokens in a document
            tokens             = self.tokenize( document )
            token_length       = len( tokens )
            truncated_document = []
            for index in range(token_length):
                if verbose:
                    print( index, tokens[index] )
                if index < max_sequence_length:
                    truncated_document.append( tokens[index] )
                else:
                    break
            tokenized_documents.extend( truncated_document )
            #num_of_tokens.append( len( tokens ) )

            if verbose:
                print( f'tokenized_documents: {tokenized_documents}' )
                print( f'truncated_document  : {truncated_document}' )

        # Compute 'vocabulary' from 'tokenized_documents'
        #   Convert the set to a list so vocabulary is easily accesible with index.
        vocabulary_set  = set( tokenized_documents )
        vocabulary      = list( vocabulary_set )  
        vocabulary_size = len( vocabulary )

        if verbose:
            print( f'      tokenized_documents: {tokenized_documents}')
            #print( f'           num_of_tokens: {num_of_tokens}')
            print( f'     truncated_vocabulary: { vocabulary}' )
        print( f'truncated_vocabulary_size: { vocabulary_size}' )
        
        return vocabulary, vocabulary_size
    
#%%
# I didn't finish this. I'm just keeping this part in case.
#    def analyze_dataframe( self, documents_df, verbose=False ):
#        '''
#        # TODO: This must be rewritten for DataFrame
#        Each row of a data frame or each review corresponds to a document.
#        documents_list is a list of documents which is equal to:
#            a column of a DataFrame or a Series converted to list or
#            a list of reviews in movie reviews for a sentiment analysis task.
#        Usage:
#            list_indexed, max_sequence_length, data_configs_df \
#              = self.nlp.analyze( documents_df )
#            
#            Note: list_indexed is a list of lists.
#        Example:
#             input
#                          documents_list: ['aa aa bb bb cc', 'aa cc dd', 'aa ee bb']
#             output
#
#        How it works:
#        # TODO: This must be rewritten for DataFrame
#        '''
#        assert isinstance( documents_df, pd.DataFrame), 'documents_df must be a pandas.DataFrame.'
#        if verbose:
#            print( 'Analyzing documents_df ...' )
#
#        tokenized_documents_list, num_of_tokens_list, vocabulary_list, token2index_dict \
#          = self.analyze_documents( documents_df, verbose )
#        
#        # Save the vocaburary to a data frame.
#        data_configs = {}  # An empty Dictionary
#        data_configs['vocab'] = pd.Series( vocabulary_list )
#        data_configs['vocab_size'] = len( vocabulary_list) +1  # +1 is for <unk> or unknown
#        
#        # Compute token_count_median to determine how many zero padding to use
#        self.upper_bound        = eda.get_upper_bound( num_of_tokens_list )
#        self.token_count_median = eda.get_median( num_of_tokens_list )
#        #max_sequence_length     = self.token_count_median
#        # max_sequence_length is median of the word counts stats.
#        # Using average may be a bad idea. Some samples with too large words
#        # may dramatically increase the value of average. 
#        
#        max_sequence_length     = math.ceil( self.token_count_median )
#        assert isinstance( max_sequence_length, int ), 'isinstance must be an integer'
#        # If max_sequence_length is a floating number, this will eventually cause an error by 
#        #   list_indexed_and_padded = pad_sequences( list_indexed_np_array, maxlen=max_sequence_length, padding='post' )
#        #   TypeError: 'numpy.float64' object cannot be interpreted as an integer
#        #   maxlen only takes an integer!
#        
#        if verbose:
#            eda.print_stat_dispersion( num_of_tokens_list, 'num_of_tokens_list')
#            print( 'token_count_median=', self.token_count_median )
#            eda.plot_histogram( num_of_tokens_list, bins=200, yscale='linear', xlim=[1,100] )
#            eda.plot_histogram( num_of_tokens_list, bins=200 )
#
#        indexed_documents_list = self.texts2sequences( documents_list, token2index_dict )
#
#        return indexed_documents_list, max_sequence_length, data_configs
    
#    def analyze_documents_dataframe( self, documents_df, verbose=True ):
#        '''
#        # TODO: This must be rewritten for DataFrame
#        Usage:
#             tokenized_documents_list, num_of_tokens_list, vocabulary_list, token2index_dict 
#               = self.analyze_documents( documents_list, verbose )
#        Example:
#             input
#                          documents_list: ['aa aa bb bb cc', 'aa cc dd', 'aa ee bb']
#             output
#                tokenized_documents_list: ['aa', 'aa', 'bb', 'bb', 'cc', 'aa', 'cc', 'dd', 'aa', 'ee', 'bb']
#                      num_of_tokens_list: [5, 3, 3]
#                         vocabulary_list: ['bb', 'cc', 'ee', 'aa', 'dd']
#                        token2index_dict: {'bb': 1, 'cc': 2, 'ee': 3, 'aa': 4, 'dd': 5}
#        How it works:
#            This function calculates in the following order.
#            
#            documents -> tokenized_documents, num_of_tokens
#                         tokenized_documents -> vocabulary
#                                                vocabulary -> token2index
#                         tokenized_documents -> tokens_count -> most_common_tokens
#        Verbose output:
#            document: aa aa bb bb cc
#            tokens  : ['aa', 'aa', 'bb', 'bb', 'cc']
#            document: aa cc dd
#            tokens  : ['aa', 'cc', 'dd']
#            document: aa ee bb
#            tokens  : ['aa', 'ee', 'bb']
#            tokenized_documents: ['aa', 'aa', 'bb', 'bb', 'cc', 'aa', 'cc', 'dd', 'aa', 'ee', 'bb']
#                  num_of_tokens: [5, 3, 3]
#                     vocabulary: ['bb', 'cc', 'ee', 'aa', 'dd']
#                vocabulary_size: 6
#                    token2index: {'bb': 1, 'cc': 2, 'ee': 3, 'aa': 4, 'dd': 5}
#                   tokens_count: Counter({'aa': 4, 'bb': 3, 'cc': 2, 'dd': 1, 'ee': 1})
#             most_common_tokens: [('aa', 4), ('bb', 3), ('cc', 2), ('dd', 1), ('ee', 1)]
#        # TODO: This must be rewritten for DataFrame
#        '''
#        assert isinstance( documents_df, pd.DataFrame), 'documents_df must be a pandas.DataFrame.'
#
#        # Compute 'tokenized_documents' & 'num_of_tokens'
#        tokenized_documents = []  # This is an empty list
#        num_of_tokens       = []  # This is an empty list
#        for index, row in documents_df.iterrows():
#            document = row['review']
#            # Above here it's dataframe
#            
#            # Make a list of tokenized_documents
#            #   tokens is a list of tokens for a document
#            #   num_of_tokens is the number of tokens in a document
#            tokens       = self.tokenize( document )
#            tokenized_documents.extend( tokens )
#            num_of_tokens.append( len( tokens ) )
#
#            if verbose:
#                print( f'document: {document}' )
#                print( f'tokens  : {tokens}' )
#
#        # Compute 'vocabulary' from 'tokenized_documents'
#        #   Convert the set to a list so vocabulary is easily accesible with index.
#        vocabulary_set  = set( tokenized_documents )
#        vocabulary      = list( vocabulary_set )  
#        vocabulary_size = len( vocabulary )
#
#        # Compute 'token2index' from 'vocabulary'
#        #   Convert the tokens to indices
#        #   Create a dictionry of tokens in the vocabulary mapped to index positions
#        token2index = {}  # This is an empty dictionary
#        # Note index starts from 1. 0 is reserved for [unk]
#        for index, token in enumerate( vocabulary, 1 ):
#            token2index[ token ] = index
#
#        # Compute 'tokens_count' from 'tokenized_documents'
#        # Just to see tokens_count.most_common()
#        tokens_count       = Counter( tokenized_documents )
#        most_common_tokens = tokens_count.most_common()
#        
#        if verbose:
#            print( f'tokenized_documents: {tokenized_documents}')
#            print( f'      num_of_tokens: {num_of_tokens}')
#            print( f'         vocabulary: { vocabulary}' )
#            print( f'    vocabulary_size: { vocabulary_size}' )
#            print( f'        token2index: {token2index}' )
#            print( f'       tokens_count: {tokens_count}' )
#            print( f' most_common_tokens: {most_common_tokens}' )
#
#        return tokenized_documents, num_of_tokens, vocabulary, token2index