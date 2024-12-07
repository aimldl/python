#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS231n Convolutional Neural Networks for Visual Recognition
http://cs231n.github.io/

Python Numpy Tutorial
http://cs231n.github.io/python-numpy-tutorial/

Numpy Reference
https://docs.scipy.org/doc/numpy/reference/
￣
python_numpy_tutorial-numpy_array_indexing.py
2019-07-02 (Tue)
"""
# Python Numpy Tutorial > Numpy > Array indexing
#   Numpy offers several ways to index into arrays.
#
# This examples cover:
#   Slicing
#   Integer array indexing
#   Boolean array indexing

#############
#  Slicing  #
#############
# Similar to Python lists, numpy arrays can be sliced.
# Since arrays may be multidimensional,
#   you must specify a slice for each dimension of the array.

import numpy as np

# Create a new array
a = np.array( [[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
#[[ 1  2  3  4]
# [ 5  6  7  8]
# [ 9 10 11 12]]

b = a[:2,1:3]
print(b)
#[[2 3]
# [6 7]]

print( a[0,1] )
#2
b[0,0] = 77
print( a[0,1] )
#77

print(a)
#[[ 1 77  3  4]
# [ 5  6  7  8]
# [ 9 10 11 12]]

print(b)
#[[77  3]
# [ 6  7]]

# You can also mix integer indexing with slice indexing.
# However, doing so will yield an array of lower rank than the original array.
# Note this is different from the way MATLAB handles array slicing.

# Create a new array # NOTE
a = np.array( [[1,2,3,4],[5,6,7,8],[9,10,11,12]]) # NOTE
print(a) # NOTE
#[[ 1  2  3  4] # NOTE
# [ 5  6  7  8] # NOTE
# [ 9 10 11 12]] # NOTE

row_r1 = a[1,:]
print( row_r1, row_r1.shape )
#[5 6 7 8] (4,)

row_r2 = a[1:2,:]             # NOTE
print( row_r2,row_r2.shape )  # NOTE: Review this again
#[[5 6 7 8]] (1, 4)           # NOTE

col_r1 = a[:,1]               # NOTE
print( col_r1,col_r1.shape )  # NOTE
# [ 2  6 10] (3,)             # NOTE

col_r2 = a[:,1:2]             # NOTE
print( col_r2,col_r2.shape )  # NOTE: Review this again
#[[ 2]                        # NOTE
# [ 6]                        # NOTE
# [10]] (3, 1)                # NOTE

############################
#  Integer array indexing  #
############################
# When you index into numpy arrays using slicing,
#   the resulting array view will always be a subarray of the original array.
# In contrast, integer array indexing allows you to construct arbitrary arrays using the data from another array. 

a = np.array( [[1,2],[3,4],[5,6]])
print(a)
#[[1 2]
# [3 4]
# [5 6]]

# An example of integer array indexing
print( a[[0,1,2],[0,1,0]] )
# [1 4 5]

# Identical to [a[0,0], a[1,1], a[2,0]]
print( np.array( [ a[0,0], a[1,1], a[2,0] ]) )
# [1 4 5]

# The same element from the source array can be used.
# in this case a[0,1] is repeated.
print( a[[0,0],[1,1]] )
# [2,2]

print( np.array( [a[0,1],a[0,1]]) )
# [2,2]

# One useful trick with integer array indexing is 
#   selecting or mutating one element from each row of a matrix:

# Create a new array
a = np.array( [[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(a)
#[[ 1  2  3]
# [ 4  5  6]
# [ 7  8  9]
# [10 11 12]]

# Create an array of indices
b = np.array( [0,2,0,1] )
print( a[ np.arange(4), b] )
# [ 1  6  7 11]
# [np.arange(4), b] means
# [ [0,1,2,3],[0,2,0,1] ]
# => a[0,0], a[1,2], a[2,0], a[3,1]

# Mutate one element from each row of a using the indices in b
a[np.arange(4),b] += 10
print(a)
#[[11  2  3]
# [ 4  5 16]
# [17  8  9]
# [10 21 12]]
# Add 10 to the indices 

############################
#  Boolean array indexing  #
############################
# Boolean array indexing lets you pick out arbitrary elements of an array.
# Frequently this type of indexing is used to select the elements of an array
#   that satisfy some condition.

a = np.array( [[1,2],[3,4],[5,6]] )
print(a)
#[[1 2]
# [3 4]
# [5 6]]

bool_idx = (a > 2)
print( bool_idx )
#[[False False]
# [ True  True]
# [ True  True]]

print( a[bool_idx] )
#[3 4 5 6]

print( a[ a>2] )
#[3 4 5 6]

print( a[ a>4] )
#[5 6]