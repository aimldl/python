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
python_numpy_tutorial-numpy_broadcasting.py
2019-07-02 (Tue)
"""
# Python Numpy Tutorial > Numpy > Broadcasting
#   When performing arithmetic operations,
#     broadcasting is a powerful mechanism that allows numpy
#     to work with arrays of different shapes.
#   Frequently we have a smaller array and a larger array, and
#     we want to use the smaller array multiple times
#     to perform some operation on the larger array.  
#   Broadcasting typically makes your code more concise and faster,
#     so you should strive to use it where possible.
#
# This examples cover:
#
#
# Read more about:
#   (full list of) universal functions that support broadcasting
#     Available ufuncs
#     https://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs
#   Explanation of this topic from different documents
#     Broadcasting
#     https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html
#     

import numpy as np


# Add a constant vector to each row of a matrix.
x = np.array( [[1,2,3],[4,5,6],[7,8,9],[10,11,12]] )
print(x)
#[[ 1  2  3]
# [ 4  5  6]
# [ 7  8  9]
# [10 11 12]]

v = np.array( [1,0,1] )
print(v)
#[1 0 1]

# Create an empty matrix with the same shape as x.
y = np.empty_like( x )
print('np.empty_like(x)=')
print(y)
#np.empty_like(x)=
#[[ 1  2  3]
# [ 4  5  6]
# [ 7  8  9]
# [10 11 12]]

# Add the vector v to each row of the matrix x
# This works; however when the matrix x is very large,
#   computing an explicit loop in Python could be slow. 
for i in range(4):
    y[i,:] = x[i,:] + v
print(y)
#[[ 2  2  4]
# [ 5  5  7]
# [ 8  8 10]
# [11 11 13]]

# Stack 4 copies of v on top of each other
vv = np.tile(v, (4,1) )
print( vv )
#[[1 0 1]
# [1 0 1]
# [1 0 1]
# [1 0 1]]

# Add x and vv elementwise
y = x + vv
print( y )
#[[ 2  2  4]
# [ 5  5  7]
# [ 8  8 10]
# [11 11 13]]

# Add v to each row of x using broadcasting
y = x + v
print( y )
#[[ 2  2  4]
# [ 5  5  7]
# [ 8  8 10]
# [11 11 13]]

# TODO: Read the following explanation cuz I'm gonna skip reading it.
#The line y = x + v works even though x has shape (4, 3) and v has shape (3,) due to broadcasting; this line works as if v actually had shape (4, 3), where each row was a copy of v, and the sum was performed elementwise.
#
#Broadcasting two arrays together follows these rules:
#
#If the arrays do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have the same length.
#The two arrays are said to be compatible in a dimension if they have the same size in the dimension, or if one of the arrays has size 1 in that dimension.
#The arrays can be broadcast together if they are compatible in all dimensions.
#After broadcasting, each array behaves as if it had shape equal to the elementwise maximum of shapes of the two input arrays.
#In any dimension where one array had size 1 and the other array had size greater than 1, the first array behaves as if it were copied along that dimension
#If this explanation does not make sense, try reading the explanation from the documentation or this explanation.

######################################
# Some applications of broadcasting  #
######################################

v = np.array( [1,2,3] )
w = np.array( [4,5] )
print(v, v.shape)
#[1 2 3] (3,)

print(w, w.shape)
#[4 5] (2,)

print( np.reshape( v,(3,1) )*w )
#[[ 4  5]
# [ 8 10]
# [12 15]]

#1*[4 5] = [4 5]
#2*[4 5] = [8 10]
#3*[4 5] = [12 15]

# Add a vector to each row of a matrix
x = np.array( [[1,2,3],[4,5,6]] )
print( x )
#[[1 2 3]
# [4 5 6]]

print( x+v )
#[[2 4 6]
# [5 7 9]]
# [1 2 3] is added to both rows. In other words,
# x has shape (2, 3) and v has shape (3,) so they broadcast to (2, 3).

print( (x.T + w ).T )
#[[ 5  6  7]
# [ 9 10 11]]

# Let's see how it worked.
print( x.T )
#[[1 4]
# [2 5]
# [3 6]]

print( x.T + w )
#[[ 5  9]
# [ 6 10]
# [ 7 11]]

# Another solution is to reshape w to a column vector shape shape (2,1).
print( x + np.reshape(w,(2,1)) )
#[[ 5  6  7]
# [ 9 10 11]]

print( np.reshape(w,(2,1)) )
#[[4]
# [5]]

# Multiply a matrix by a constant
print( x*2 )
#[[ 2  4  6]
# [ 8 10 12]]