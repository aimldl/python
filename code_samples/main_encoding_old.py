#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
main_encoding.py
# Sentiment Indentification for Roman Urdu

## Word representation technique
The goal of this part is to obtain:
  the encoded text along with the corresponding class labels and ids.
    The goal can be explained the best with an example.

df_preproc is a dataframe of preprocessed text.
Each row of the 'review' column consists of tokens of text.
It's the input to encoder.encode_text_from.
Say the input data is a dummy input. 
         id sentiment   review
    0     0         2     cc zz yy
    1     2         1     zz bb yy rr
    2     3         0     yy rr aa zz
    3     4         2     zz cc rr
    4     5         1     zz bb rr
    5     7         0     aa zz
    6     8         1     zz bb
    7    10         1     zz yy rr

Note the first column is the (true) index of this dataframe while
     the 'id' column is the id of the original dataframe BEFORE preprocessing.
     Some rows are removed from the original dataframe during preprocessing.

encoder.encode_text_from converts the 'review' column to integers 
The length is bound to max_document_length which is 7 in this case.
A review shorter than max_document_length is padded with zeros.

        id sentiment  0  1  2  3  4  5  6
    0     0         2    3  6  5  0  0  0  0
    1     2         1    6  2  5  4  0  0  0
    2     3         0    5  4  1  6  0  0  0
    3     4         2    6  3  4  0  0  0  0
    4     5         1    6  2  4  0  0  0  0
    5     7         0    1  6  0  0  0  0  0
    6     8         1    6  2  0  0  0  0  0
    7    10         1    6  5  4  0  0  0  0
    
df_vocab
   id vocabulary  count
0   0      [unk]      0
1   1         aa      2
2   2         bb      3
3   3         cc      2
4   4         rr      5
5   5         yy      4
6   6         zz      8
'''

import os
import logging
import time
import numpy as np
import pandas as pd
from   collections import Counter

# Custom modules
import configuration
import util_fns
import functions4nlp
import text_encoding
import input_dataframe

    #%%
if __name__ == '__main__':
    verbose     = True
    #verbose     = False
    debug        = True
    #debug       = False
    dummy_input = True
    #dummy_input = False
    
    count_threshold_min = 0
    count_threshold_max = 4
    
    print( 'Loading the preprocessed data...')
    
    #######################
    # Directories & Files #
    #######################
    #dir_input = '../output/2019-08-12'
    dir_input  = '../output/'
    dir_output = '../output'

    # Input file
    #   The input file is in directory ../output
    #   because the output of the previous result is imported here.
    file_name_input = 'df_preproc.csv'
    file_input      = os.path.join( dir_input, file_name_input )
    print( '  file_input =', file_input )

    file_name_vocab  = 'df_vocab.csv'
    file_vocab       = os.path.join( dir_output, file_name_vocab )
    print( '  file_vocab =', file_vocab )

    # Output files
    file_name_filtered_text = 'df_filtered_text.csv'
    file_filtered_text      = os.path.join( dir_output, file_name_filtered_text )
    
    file_name_duplicated = 'df_duplicated.csv'
    file_duplicated      = os.path.join( dir_output, file_name_duplicated )
    
    file_name_encoded_text = 'df_encoded_text.csv'
    file_encoded_text      = os.path.join( dir_output, file_name_encoded_text )
    if verbose:
        print( '  file_filtered_text =', file_filtered_text )
        print( '  file_encoded_text =', file_encoded_text )

    ##########################
    # Initialize & Configure #
    ##########################
    config  = configuration.Configuration()
    nlp     = functions4nlp.Nlp()
    encoder = text_encoding.TextEncoding()

    #%%####################
    # Load the Input Data #
    #######################
    if dummy_input:
        df_preproc = input_dataframe.dummy_input( verbose )
#        dummy_review_list     = ['cc zz yy', 'zz bb yy rr', 'yy rr aa zz', 'zz cc rr', 'zz bb rr', 'aa zz', 'zz bb', 'zz yy rr']
#        dummy_sentiment_list = ['2', '1', '0', '2', '1', '0', '1', '1']
#        dummy_index_list     = ['0', '2', '3', '4', '5', '7', '8', '10']
#        
#        df_preproc = pd.DataFrame( dummy_index_list, columns=['old_index'] )
#        df_preproc = df_preproc.assign( sentiment = dummy_sentiment_list)
#        df_preproc = df_preproc.assign( review = dummy_review_list)

        df_vocab, vocab_size, tokens_list, num_of_tokens_list, token2id_dict \
          = nlp.compute_vocab_and_tokens_from( df_preproc, count_threshold_min, count_threshold_max, verbose, debug, dummy_input )
        df_vocab, vocab_size, tokens_list, num_of_tokens_list, token2id_dict \
          = nlp.compute_vocab_and_tokens_from( df_preproc, verbose, debug, dummy_input )

    else:
        # Load the output of the previous step: df_preproc
        #   df_preproc = preproc.preprocess( df_tidy, verbose, debug=False )
        #   df_preproc.to_csv( file_preproc, index=None )  #, header=None )
    
        # header=0 is important! Otherwise, the column names are messed up.
        df_preproc = pd.read_csv( file_input, header=0, delimiter=',' )
        #print( df_preproc.shape )
        #print( df_preproc.head() )
        '''
           id  sentiment                                             review
        0      0          0  guzishta arse deal stain musalsal kai bar aap ...
        1      1          0      akhri runs zarorat sorat e hall one day match
        2      2          0  musbat faisla jahan unki sakhsiyat mazeed must...
        3      3          0                           bohot say ilazmat lagaye
        4      4          0  apne khilaf tehrik e adam etemad nakam hone ba...
        '''
        if debug:
            print(f'Loaded {file_input} to df_preproc')
    
        # Load the output of the previous step: df_preproc
        #   df_vocab, vocab_size, tokens_list, num_of_tokens_list, token2id_dict \
        #     = nlp.compute_vocab_and_tokens_from( df_preproc, verbose, debug, dummy_input )
        #   df_vocab.to_csv( file_vocab, index=None )  #, header=None )
    
        df_vocab = pd.read_csv( file_vocab )  #, names=['id','review'], delimiter=',' )
        #print( df_vocab.shape )
        #print( df_vocab.head() )
        if debug:
            print(f'Loaded {file_vocab} to file_vocab')

    print( '  df_preproc.shape =', df_preproc.shape )
    print( df_preproc.head(3) )
    if verbose:
        print( df_preproc.tail(3) )

    print( '  df_vocab.shape =', df_vocab.shape )
    print( df_vocab.head(3) )
    if verbose:
        print( df_vocab.tail(3) )

    #%%###########################
    # Encode the Text Input Data #
    ##############################
    
    encoder.test_keys( df_vocab, verbose, debug, dummy_input )
    
    # The filtering process
    #   (1) out-of-vocabulary tokens are converted to '[unk]' or unknown.
    #   (2) duplicate reviews are removed.
    #       Note: 839 duplicates are created. For example,
    #             there're so many reviews with a single '[unk]'.
    #   Refer to 
    #     file_duplicated = '../output/df_duplicated.csv'
    #   to review the duplicates
    
    # I thought of moving 'filter_unknown_vocab_from' to class TextPreProcessing.
    # But it uses df_vocab which is created by class Nlp.
    # Logically, it may stay either class TextEncoding or TextPreProcessing.
    # I think it's better to be in class TextEncoding. 
    
    max_token_length = 20
    df_filtered_text, df_duplicated = encoder.filter_unknown_vocab_from( df_preproc, df_vocab, max_token_length, verbose, debug, dummy_input )
    df_filtered_text.to_csv( file_filtered_text )
    print('Saved to', file_filtered_text)
    print( '  df_filtered_text =', df_filtered_text.shape )
    print( df_filtered_text.head(3) )
    
    df_duplicated.to_csv( file_duplicated )
    print('Saved to', file_duplicated)
    print( '  df_duplicated =', df_duplicated.shape )
    print( df_duplicated.head(3) )
    
    df_encoded_text = encoder.encode_text_from( df_filtered_text, df_vocab, max_token_length, verbose, debug, dummy_input )
    df_encoded_text.to_csv( file_encoded_text, index=None )  #, header=None )
    print('Saved to', file_encoded_text)
    print( '  df_encoded_text =', df_encoded_text.shape )
    print( df_encoded_text.head(3) )

    if debug:
        input( 'Enter to proceed:' )
    else:
        sec2pause = 20  # seconds
        print( 'Pause for', sec2pause, 'second(s)' )
        time.sleep( sec2pause )
# EOF
    
    # TODO: remove some vocabularies starting from numbers, ones with _, and so on.    
    # TODO: Balance the class labels

    #cv = CountVectorizer( min_df=0, max_df=1.)
    #cv_matrix = cv.fit_transform( norm_corpus )
    #cv_matrix = cv_matrix.toarray( documents_list )
    #print( cv_matrix )
            

        #%%#############
        # TF-IDF Model #
        ################
        # term frequency (tf) and inverse document frequency (idf)
        #   tfidf = tf x idf
    #    tv = TfidfVectorizer( min_df = 0., max_df=1., use_idf=True )
    #    tv_matrix = tv.fit_transform( norm_corpus )
    #    tv_matrix = tv_matrix.toarray()
    #    print( tv_matrix )



# TODO
#        vocalubrary = set( words )
#        print('-'*70)
#        print( vocalubrary )
#        print('-'*70)
#        print( words )
#        print('-'*70)
#        print( 'word/vocab ratio=', len(words)/len(vocalubrary) ) 
    
    #***
#    # Most common vocabularies in three sentiments are analyzed.
#    # Allah, for example, is included in all of the sentiments so frequently that
#    # this vocabulary may not contribute to distinguish the three classes by a neural net.
#    
#    # ***
#    #15817,2,good bad team
#    ided_documents_list = self.texts2sequences( documents_list, token2id_dict )
#
#    
#    # data_configs_df, list_ided
#    ided_and_padded_df.to_csv( file_ided_and_padded, index=None, header=None )
#    if verbose:
#        print( f'Saved to {file_ided_and_padded}' )
#
#
##    ided_and_padded_df = pd.DataFrame( list_ided_and_padded )
#
#    ided_and_padded_df.to_csv( file_ided_and_padded, index=None, header=None )
#    if verbose:
#        print( f'Saved to {file_ided_and_padded}' )
#    
##    utils.save_dict2csv( vocaburary_dict, file_vocab )