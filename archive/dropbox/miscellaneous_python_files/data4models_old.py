#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
'''
data4models.py
# Sentiment Indentification for Roman Urdu
'''
 
import numpy as np
 
class Data:
    # Constructor
    def __init__( self, x, y, config ):
        self.config = config
        self.x      = x # shape = (length, dimension)
        self.y      = y # shape = (length,)
        
    def split( self, split_rate=0.8 ):
        length, dimension = np.shape( self.x )
   
        # Split the (entire) data into training data & test data
        n_training = int( length * split_rate )  # 0.8
        n_test     = length - n_training  # 0.2
 
        # Use indexcing to split the data.
        index_data     = np.arange( length )  # [0, length-1]
        index_training = np.random.choice( length, n_training, replace=False )
        index_test     = np.delete( index_data, index_training )
         
        self.data_training   = self.x[ index_training, : ]
        self.data_test       = self.x[ index_test, : ]
         
        self.labels_training = self.y[ index_training ]
        self.labels_test     = self.y[ index_test ]
 
        #=====================================================================#
        # The above variables don't have the leading self. to improve readability.
        self.length     = length  # = size, or n_data
        self.dimension  = dimension
         
        self.n_training = n_training
        self.n_test     = n_test

     
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