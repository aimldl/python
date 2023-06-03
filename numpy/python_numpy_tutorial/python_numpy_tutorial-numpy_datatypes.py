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
python_numpy_tutorial-numpy_datatypes.py
2019-07-02 (Tue)
"""
# Python Numpy Tutorial > Numpy > Datatypes
#   Every numpy array is a grid of elements of the same type.
#   Numpy provides a larget set of numeric datatypes
#     that you can use to construct arrays.
#   Numpy tries to guess a datatype when you create an array, but
#     functions that construct arrays usually also include an optional argument
#     to explicitly specify the datatype.
#
# This examples cover:
#   dtype
#
# Read more about numpy datatypes here.
#   Data type objects (dtype)
#   https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html

import numpy as np

x = np.array( [1,2] )
print( x )
#[1 2]
print( x.dtype )
#int64

x = np.array( [1,2], dtype=np.int64 )
print( x )
#[1 2]
print( x.dtype )
#int64

x = np.array( [1.0,2.0] )
print( x )
#[1. 2.]
print( x.dtype )
#float64