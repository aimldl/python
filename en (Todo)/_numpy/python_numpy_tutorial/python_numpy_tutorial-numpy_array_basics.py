#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS231n Convolutional Neural Networks for Visual Recognition
http://cs231n.github.io/

Python Numpy Tutorial
http://cs231n.github.io/python-numpy-tutorial/
￣
python_numpy_tutorial-numpy_array_basics.py
2019-07-02 (Tue)
"""
# Python Numpy Tutorial > Numpy > Arrays
#   Numpy is the core library for scientific computing in Python.
#   It provides a high-performance multidimensional array object, and tools for working with these arrays.
#   If you are already familiar with MATLAB, you might find this tutorial useful to get started with Numpy.
#
# This examples cover:
#   initialization
#   accessing elements

import numpy as np

# Initialize numpy arrays from nested Python lists
a = np.array( [1,2,3] )
print( type(a) )
# <class 'numpy.ndarray'>
print( a.shape )
# (3,)

# Access elements using squared brackets just like an array
print( a[0],a[1],a[2] )
# 1 2 3
a[0] = 5
print(a)
# [5 2 3]

b = np.array( [[1,2,3],[4,5,6]] )
print(b.shape)
# (2, 3)
print(b[0,0],b[0,1],b[1,0])
# 1 2 4

# Functions to create arrays
# an array of all zeros
a = np.zeros( (2,2) )
print(a)
#[[0. 0.]
# [0. 0.]]

# an array of all ones
b = np.ones( (1,2) )
print(b)
# [[1. 1.]]

# Constant array 2x2 filled with 7
c = np.full( (2,2),7 )
print(c)
#[[7 7]
# [7 7]]

# Identity matrix 2x2
d = np.eye(2)
print(d)
#[[1. 0.]
# [0. 1.]]

# Random values 2x2
e = np.random.random( (2,2) )
print(e)
#[[0.77683074 0.04332916]
# [0.4476379  0.60276708]]