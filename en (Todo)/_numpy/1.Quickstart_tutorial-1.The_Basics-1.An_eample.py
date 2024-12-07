# 1.Quickstart_tutorial-1.The_Basics-1.An_eample.py
#
# https://docs.scipy.org/doc/numpy/user/quickstart.html
# The Basics - An example

import numpy as np

a = np.arange(15).reshape(3,5)
#>>> a
#array([[ 0,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9],
#       [10, 11, 12, 13, 14]])

print( a.shape )
#(3, 5)

print( a.ndim )
#2

print( a.dtype.name )
#int64

print( a.itemsize )
#8

print( a.size )
#15

print( type(a) )
#<class 'numpy.ndarray'>

b = np.array( [6,7,8] )
#array([6, 7, 8])

print( type(b) )
#<class 'numpy.ndarray'>
