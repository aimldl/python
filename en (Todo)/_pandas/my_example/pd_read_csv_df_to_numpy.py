'''
Read a dataframe into a numpy array.
'''

import os
import numpy as np
import pandas as pd

if __name__ == '__main__':

    dir_input  = 'input'
    filename   = 'example.csv'
    file       = os.path.join( dir_input, filename )
    
    df         = pd.read_csv( file, header=0 )
    data_np    = df.to_numpy()    
#    array([[22338, 11479, 26706, ...,  6647,     0,     0],
#           [ 7144,  8366, 12232, ..., 26923, 25935, 27134],
#           [25235, 26195, 11457, ...,     0,     0,     0],
#           ...,
#           [30140, 12388,  8489, ...,     0,     0,     0],
#           [14151,  9603,  5506, ...,     0,     0,     0],
#           [10946,  1203, 20637, ...,     0,     0,     0]], dtype=int64)
