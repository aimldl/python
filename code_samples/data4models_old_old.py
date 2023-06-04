#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
'''
data4models.py
# Sentiment Indentification for Roman Urdu
'''
 
import numpy  as np
import pandas as pd
 
class Data:
    # Constructor
    def __init__( self, config ):
        self.config = config

    def split( self, df ):
        '''
        Split the (entire) data into training data & test data
        '''
        assert isinstance( df, pd.DataFrame), 'df must be a pandas.DataFrame.'

        test_split_ratio = self.config.test_split_ratio
        print(f'Data.preprocess.split: test_split_ratio= {test_split_ratio}' )
        
        reviews    = df['review']
        sentiments = df['sentiment']

        n_dataset  = df.shape[0]
        n_test     = int( n_dataset * test_split_ratio )  # 0.7
        n_training = n_dataset - n_test                   # 0.3
 
        # Use indexcing to split the data.
        index_data     = np.arange( n_dataset )
        index_training = np.random.choice( index_data, n_training, replace=False )
        index_test     = np.delete( index_data, index_training )
         
        data_training_np = reviews.loc[ index_training ].values
        data_test_np     = reviews.loc[ index_test ].values
         
        labels_training_np = sentiments.loc[ index_training ].values
        labels_test_np     = sentiments.loc[ index_test ].values
        
        print(f'  number of dataset =', n_dataset )
        print(f'  np.shape(x_train) =', np.shape(data_training_np) )
        print(f'  np.shape(y_train) =', np.shape(labels_training_np) )
        print(f'   np.shape(x_test) =', np.shape(data_test_np) )
        print(f'   np.shape(y_test) =', np.shape(labels_test_np) )
        
        return data_training_np, labels_training_np, data_test_np, labels_test_np
        # x_train, y_train, x_test, y_test

#    def __init__( self, x, y, config ):
#        self.config = config
#        self.x      = x # shape = (length, dimension)
#        self.y      = y # shape = (length,)
    def split( self, split_rate=[0.7, 0.2, 0.1] ):
        '''
        The default ratio to split the training, evaluation, & test data is 7:2:1.
        '''
        print( 'split_rate = ', split_rate )
        
        length, dimension = np.shape( self.x )
   
        # Split the (entire) data into training data & test data
        n_training   = int( length * split_rate[0] )  # 0.7
        n_evaluation = int( length * split_rate[1] )  # 0.2
        n_test       = length - n_training - n_evaluation
 
        # Use indexcing to split the data.
        index_data       = np.arange( length )  # 13704, [0, length-1]
        index_training   = np.random.choice( index_data, n_training, replace=False )  # 9592
        index_temp       = np.delete( index_data, index_training )  # 4112
        
        index_evaluation = np.random.choice( index_temp, n_evaluation ) # 2740
        index_test       = np.delete( index_temp, index_evaluation )  # 3547, This must be 1372!
         
        data_training   = self.x[ index_training, : ]
        data_evaluation = self.x[ index_evaluation, : ]
        data_test       = self.x[ index_test, : ]
         
        labels_training   = self.y[ index_training ]
        labels_evaluation = self.y[ index_evaluation ]
        labels_test       = self.y[ index_test ]
        
        training   = [data_training, labels_training]
        evaluation = [data_evaluation, labels_evaluation]
        test       = [data_test, labels_test]
     
        return training, evaluation, test
    
#        #=====================================================================#
#        # The above variables don't have the leading self. to improve readability.
#        self.length     = length  # = size, or n_data
#        self.dimension  = dimension
#         
#        self.n_training = n_training
#        self.n_test     = n_test

     
    def load(self, batch_size):
        data_length = len( self.data_training )
        
        if data_length >= batch_size:
            # Because of replace=False, 
            # ValueError: Cannot take a larger sample than population when 'replace=False'
            
            index  = np.random.choice( data_length, batch_size, replace=False )
            data   = self.data_training[ index,: ]
            labels = self.labels_training[ index ]
             
            self.data_training   = np.delete( self.data_training, index, axis=0 )
            self.labels_training = np.delete( self.labels_training, index )
            done = True
        else: #data_length < batch_size:
            self.data_training   = self.x[ self.index_training ]
            self.labels_training = self.y[ self.index_training ]
            done = False
         
        return data, labels, done
 
# EOF