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
python_numpy_tutorial-numpy_array_math.py
2019-07-02 (Tue)
"""
# Python Numpy Tutorial > Numpy > Array Math
#   Basic math functions operate elementwise on arrays.
#   In the numpy module, they're available both as
#     operator overloads and as functions.
#
# This examples cover:
#   Basic Math Functions
#     Elementwise sum         x+y or np.add(x,y)
#     Elementwise subtraction x-y or np.subtract(x,y)
#     Elementwise product     x*y or np.multiply(x,y)
#     Elementwise division    x/y or np.divide(x,y)
#     Elementwise square root        np.sqrt(x)
#   Inner Product 'dot
#     Inner product of vectors
#     Matrix-vector product
#     Matrix-matrix product
#     sum (as an example of math functions in numpy)
#
# Read more about:
#   numpy's full list of math functions
#     Mathematical functions
#     https://docs.scipy.org/doc/numpy/reference/routines.math.html
#   array manipulation routines
#     Array manipulation routines
#     https://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html

import numpy as np

##########################
#  Basic Math Functions  #
##########################

x = np.array( [[1,2],[3,4]], dtype=np.float64 )
y = np.array( [[5,6],[7,8]], dtype=np.float64 )
print( x )
#[[1. 2.]
# [3. 4.]]

print( y )
#[[5. 6.]
# [7. 8.]]

# Elementwise sum
print( x+y )
#[[ 6.  8.]
# [10. 12.]]

print( np.add(x,y) )
#[[ 6.  8.]
# [10. 12.]]

# Elementwise subtraction
print( x-y )
#[[-4. -4.]
# [-4. -4.]]

print( np.subtract(x,y) )
#[[-4. -4.]
# [-4. -4.]]

# Elementwise product
print( x*y )
#[[ 5. 12.]
# [21. 32.]]

print( np.multiply(x,y) )
#[[ 5. 12.]
# [21. 32.]]

# Elementwise division
print( x/y )
#[[0.2        0.33333333]
# [0.42857143 0.5       ]]

print( np.divide(x,y) )
#[[0.2        0.33333333]
# [0.42857143 0.5       ]]

# Elementwise square root
print( np.sqrt(x) )
#[[1.         1.41421356]
# [1.73205081 2.        ]]

#########################
#  Inner Product 'dot'  #
#########################
# Unlike MATLAB, * is elementwise multiplication,
#   not matrix multiplication.
# Instead, the dot function is used to compute
#   inner products of vectors,
#   to multiply a vector by a matrix, and
#   to multiply matrices.
# Dot is available both
#   as a function in the numpy module and
#   as an instance method of array objects.

x = np.array( [[1,2],[3,4]]  )
print(x, x.shape)
#[[1 2]
# [3 4]] (2, 2)

y = np.array( [[5,6],[7,8]] )
print(y, y.shape)
#[[5 6]
# [7 8]] (2, 2)

v = np.array( [9,10] )
print(v, v.shape)
#[ 9 10] (2,)

w = np.array( [11,12] )
print(w, w.shape)
#[11 12] (2,)

# Inner product of vectors
print( v.dot(w) )
# 219
# [9 10] [11 12] = 9*11+10*12 = 99 + 120 = 219

print( np.dot(v,w) )
# 219

# Matrix-vector product
#   x v = (2x2) x (2x1) = (2x1)
#   rank 1 array is procuded.
print( x.dot(v) )
# [29 67]

print( np.dot(x,v) )
# [29 67]

# Matrix-matrix product
#   produce rank 2 array.
print( x.dot(y) )
#[[19 22]
# [43 50]]

print( np.dot(x,y) )
#[[19 22]
# [43 50]]

#####################################
# NOTE: numpy math functions 'sum'  #
#####################################

x = np.array( [[1,2],[3,4]] )  # NOTE
print(x)                       # NOTE
#[[1 2]                        # NOTE
# [3 4]]                       # NOTE

print( np.sum(x) )             # All elements
#10

print( np.sum(x,axis=0) )      # Each column # NOTE
#[4 6]                         # NOTE

print( np.sum(x,axis=1) )      # Each row # NOTE
# [3 7]                        # NOTE

##########################
#  Transposing a matrix  #
##########################

x = np.array( [[1,2],[3,4]]  )
print(x)
#[[1 2]
# [3 4]]

print(x.T)
#[[1 3]
# [2 4]]

# NOTE: Taking the transpose of a rank 1 array DOES NOTHING!
v = np.array([1,2,3])  # NOTE
print(v, v.shape)      # NOTE
#[1 2 3] (3,)          # NOTE

print(v.T, v.T.shape)  # NOTE
#[1 2 3] (3,)          # NOTE