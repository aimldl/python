#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
input_dataframe.py
# Sentiment Indentification for Roman Urdu
"""

import pandas as pd

#%%
def dummy_input( verbose=False ):
    '''
    returns a dummy dataframe 'df_preproc' used as a dummy input for debugging.
    
    dummy vocabulary:
        aa is only in 0.
        bb is only in 1.
        cc is only in 2.
        rr is included randmly.
        yy are in all classes.
        zz are in all classes.
        
    CAUTION:
      The index of ae new dataframe will be messed up
        if 'index' is used for the column name.
      So the column name is 'old_index'.
      The values in the 'old_index' is not consecutive
        because some values are dropped by drop_duplicates.
    '''
    print( 'dummy_input: Preparing a dummy input', end='' )
    dummy_review_list    = ['cc zz yy',
                            'zz bb yy rr',
                            'yy rr aa zz',
                            'zz cc rr',
                            'zz bb rr',
                            'aa zz',
                            'zz bb',
                            'zz yy rr']
    dummy_sentiment_list = ['2', '1', '0', '2', '1', '0', '1', '1']
    dummy_index_list     = ['0', '2', '3', '4', '5', '7', '8', '10']

    df_preproc = pd.DataFrame( dummy_index_list, columns=['old_index'] )
    df_preproc.index.name = 'index'
    df_preproc = df_preproc.assign( sentiment = dummy_sentiment_list)
    df_preproc = df_preproc.assign( review = dummy_review_list)
    
    print( 'of size', df_preproc.shape )
    if verbose:
        print( df_preproc )
        print('Loaded a dummy input.')
    
    return df_preproc
# EOF