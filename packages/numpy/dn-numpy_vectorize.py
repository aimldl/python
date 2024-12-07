#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dn-numpy_vectorize.py
[numpy.vectorize](https://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html)

class numpy.vectorize(pyfunc, otypes=None, doc=None, excluded=None, cache=False, signature=None)[source]

Define a vectorized function which takes a nested sequence of objects or numpy arrays as inputs 
  and returns a single numpy array or a tuple of numpy arrays. 
The vectorized function evaluates pyfunc over successive tuples of the input arrays 
  like the python map function, except it uses the broadcasting rules of numpy.

Notes
The vectorize function is provided primarily for convenience, not for performance.
The implementation is essentially a for loop.

Parameters:	
pyfunc : callable
  A python function or method.

otypes : str or list of dtypes, optional
  The output data type. It must be specified as either a string of typecode characters or a list of data type specifiers. There should be one data type specifier for each output.

doc : str, optional
  The docstring for the function. If None, the docstring will be the pyfunc.__doc__.

excluded : set, optional
  Set of strings or integers representing the positional or keyword arguments for which the function will not be vectorized. These will be passed directly to pyfunc unmodified.
  New in version 1.7.0.

cache : bool, optional
  If True, then cache the first function call that determines the number of outputs if otypes is not provided.
  New in version 1.7.0.

signature : string, optional
  Generalized universal function signature, e.g., (m,n),(n)->(m) for vectorized matrix-vector multiplication. If provided, pyfunc will be called with (and expected to return) arrays with shapes given by the size of corresponding core dimensions. By default, pyfunc is assumed to take scalars as input and output.
  New in version 1.12.0.

Returns:	
  vectorized : callable
  Vectorized function.  

"""
#%%#########
# Examples #
############

import numpy as np

#%%#######
# pyfunc #
##########
def myfunc(a,b):
    "Return a-b if a>b, otherwise return a+b"
    if a>b:
        return a-b
    else:
        return a+b

vfunc = np.vectorize( myfunc )
result = vfunc( [1,2,3,4], 2)
print( type(result) )
# <class 'numpy.ndarray'>
print( result )
# [3 4 1 2]

#%%#######
# otypes #
##########

out = vfunc( [1,2,3,4], 2)
print( type(out) )
# <class 'numpy.ndarray'>
print( type(out[0]) )
# <class 'numpy.int64'>

print( out[0] )
# 3

#%%####
# doc #
#######
# Change the explanation with __doc__

print( vfunc.__doc__ )
# Return a-b if a>b, otherwise return a+b

vfunc = np.vectorize(myfunc, doc='Vectorized `myfunc`')
print( vfunc.__doc__ )
# Vectorized `myfunc`

#%%#########
# excluded #
############
# Excluded argument
#   can be used to prevent vectorizing over certain arguments.
# This can be useful for array-like arguments of 
#  a fixed length such as the coefficients for a polynomial as in polyval:

def mypolyval(p,x):
    _p  = list(p)
    res = _p.pop(0)
    while _p:
        res = res*x + _p.pop(0)
    return res

vpolyval = np.vectorize(mypolyval, excluded=['p'])
print( vpolyval(p=[1, 2, 3], x=[0, 1]) )
# [3 6]

vpolyval.excluded.add(0)
print( vpolyval(p=[1, 2, 3], x=[0, 1]) )
# [3 6]

#%%######
# cache #
#########
# has no example

#%%##########
# signature #
#############
# The signature argument allows for vectorizing functions 
#   that act on non-scalar arrays of fixed length. 

###################################
# Pearson correlation coefficient #
###################################
# For example, you can use it for a vectorized calculation of 
#   Pearson correlation coefficient and its p-value:
import scipy.stats

pearsonr = np.vectorize( scipy.stats.pearsonr,
                         signature='(n),(n)->(),()')
print( pearsonr([[0, 1, 2, 3]], [[1, 2, 3, 4], [4, 3, 2, 1]]) )
# (array([ 1., -1.]), array([0., 0.]))

##########################
# Vectorized convolution #
##########################
# Another example

convolve = np.vectorize( np.convolve, signature='(n),(m)->(k)')
print( convolve( np.eye(4),[1,2,1] ) )
#[[1. 2. 1. 0. 0. 0.]
# [0. 1. 2. 1. 0. 0.]
# [0. 0. 1. 2. 1. 0.]
# [0. 0. 0. 1. 2. 1.]]

