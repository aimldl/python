#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GeeksforGeeks-numpy_in_python-set_1-introduction-2_array_creation.py
￣
GeeksforGeeks
https://www.geeksforgeeks.org/

NumPy in Python | Set 1 (Introduction)
(Contributed by Nikhil Kumar.)
https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/

To read more about the related topics,
  NumPy Reference
  https://docs.scipy.org/doc/numpy-1.10.1/reference/index.html

￣
2019-07-04 (Thu)
"""
# Numpy in Python > Introduction > 2.Array Creation

# This example covers:
#   1. Arrays in Numpy
#     creation (from a list)
#     type
#     ndim
#     shape
#     size
#     dtype
#
#   2. Array creation
#     from a list
#     from a tuple
#     zeros
#     *ones
#     full
#     *empty  No example presented by the tutorial. So I added examples by myself
#     random
#     arange
#     linspace
#     reshape
#     flatten
#
#   3. Array Indexing
#     Slicing
#     Integer array indexing
#     Boolean array indexing
#
#   4. basic operations
#     Operations on single array
#     Unary operators
#     Universal functions (ufunc)
#     
#   5. Sorting array
#     np.sort( arr ), sort the array (row-wise)
#     axis=1, row-wise sorting
#     axis=0, column-wise sorting
#     kind='mergesort', selecting the sorting method with 
#     axis=None, flatten and sort the all elements
#     sort a structured array
#     order='name' defined by dtypes
#     order=['grad_year','cgpa'] defined by dtypes
# Read more about:
#   numpy.empty
#   https://docs.scipy.org/doc/numpy/reference/generated/numpy.empty.html
#
#    Recommended Posts:
#    Python | Numpy numpy.ndarray.__ne__()
#    Python | Numpy numpy.ndarray.__and__()
#    Python | Numpy numpy.ndarray.__neg__()
#    Python | Numpy numpy.ndarray.__isub__()
#    Python | Numpy numpy.ndarray.__pos__()
#    Python | Numpy numpy.ndarray.__iadd__()
#    Python | Numpy numpy.ndarray.__xor__()
#    Python | Numpy numpy.ndarray.__eq__()
#    Python | Numpy numpy.ndarray.__ge__()
#    Python | Numpy numpy.ndarray.__imul__()
#    Python | Numpy numpy.ndarray.__lshift__()
#    Python | Numpy numpy.ndarray.__rshift__()
#    Python | Numpy numpy.ndarray.__pow__()
#    Python | Numpy numpy.ndarray.__divmod__()
#    Python | Numpy numpy.ndarray.__invert__()

import numpy as np

line="-" * 30

#====================================================================
print("1. Arrays in Numpy")
print( line )

arr = np.array( [[1,2,3],[4,2,5]] )
print("type=", type(arr))
#type= <class 'numpy.ndarray'>
print("number of dimensions=", arr.ndim)
#number of dimensions= 2
print("Shape=", arr.shape)
#Shape= (2, 3)
print("Size=", arr.size)
#Size= 12
print("Data type=", arr.dtype)
#Data type= int64

#====================================================================
print("2. Array creation")
print( line )

a = np.array( [[1,2,4],[5,8,7]], dtype='float' )
print("Array created from list with type float\n",a)
# [[1. 2. 4.]
# [5. 8. 7.]]

b = np.array( (1,3,2) )
print("Array created from tuple\n",b)
# [1 3 2]

c = np.zeros( (3,4) )
print("3x4 array initialized with all zeros\n", c)
# [[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]

d = np.full( (3,3),6,dtype='complex')
print("3x3 array initialized with all 6s\n", d)
# [[6.+0.j 6.+0.j 6.+0.j]
# [6.+0.j 6.+0.j 6.+0.j]
# [6.+0.j 6.+0.j 6.+0.j]]

# These empty examples are not in the tutorial.
# So I added them by myself.
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.empty.html
d_empty = np.empty( (2,2) )
print("2x2 array initialized with empty\n", d_empty)
# [[1.9044942e-316 0.0000000e+000]
# [0.0000000e+000 0.0000000e+000]]

# [] works, too
d_empty_square = np.empty( [2,2] )
print("2x2 array initialized with empty\n", d_empty_square)
# [[1.9044942e-316 0.0000000e+000]
# [0.0000000e+000 0.0000000e+000]]

d_empty_int = np.empty( (2,2), dtype='int')
print("2x2 array initialized with empty\n", d_empty_int)
# [[38547392        0]
# [       0        0]]
 
d_empty_complex = np.empty( (2,2), dtype='complex')
print("2x2 array initialized with empty\n", d_empty_complex)
# [[0.0e+000+1.06718180e-321j 0.0e+000+2.03676547e-316j]
# [1.4e-322+6.91236450e-310j 4.9e-324+0.00000000e+000j]]

e = np.random.random( (2,2) )
print("2x2 array initialized with random numbers\n", e)
# [[0.33910781 0.9765249 ]
# [0.4583446  0.91109638]]

f = np.arange(0,30,5)
print("A sequential array: 0 to 30 with steps of 5\n", f)
# [ 0  5 10 15 20 25]
# Note 30 is missing.

g = np.linspace(0,5,10)
print("A sequential array: 0 to 5 with 10 values in-between\n", g)
#[0.         0.55555556 1.11111111 1.66666667 2.22222222 2.77777778
# 3.33333333 3.88888889 4.44444444 5.        ]

arr = np.array( [[1,2,3,4],[5,2,4,2],[1,2,0,1]] )
print("Original array: 3x4 array has 12 elements in total\n", arr)
# [[1 2 3 4]
# [5 2 4 2]
# [1 2 0 1]]

newarr = arr.reshape(2,2,3)
print("Reshaped array: 2x2x3 array has 12 elements, too\n", newarr)
# [[[1 2 3]
#  [4 5 2]]
#
# [[4 2 1]
#  [2 0 1]]]

arr = np.array( [[1,2,3],[4,5,6]] )
flarr = arr.flatten()
print("Original array\n",arr)
# [[1 2 3]
# [4 5 6]]
print("Flattened array\n",flarr)
# [1 2 3 4 5 6]

#====================================================================
print("3. Array Indexing")
print( line )

arr = np.array( [[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]] )
print(arr)
#[[-1.   2.   0.   4. ]
# [ 4.  -0.5  6.   0. ]
# [ 2.6  0.   7.   8. ]
# [ 3.  -7.   4.   2. ]]

# Slicing array
temp = arr[:2, ::2]
print("first two rows & alternate columns (0,2)\n",temp)
#[[-1.  0.]
# [ 4.  6.]]

# Integer array indexing
temp = arr[[0,1,2,3],[3,2,1,0]]
print("arr[0,3],arr[1,2], arr[2,1], arr[3,0]")
print( temp )
#[4. 6. 0. 3.]

# Boolean array indexing
idx = arr > 0  # Indices for the element bigger than 0
print( idx )
#[[False  True False  True]
# [ True False  True False]
# [ True False  True  True]
# [ True False  True  True]]

# temp is a sequence selected from arr.
temp = arr[idx]
print( temp )
# [2.  4.  4.  6.  2.6 7.  8.  3.  4.  2. ]

#====================================================================
print("4. Basic Operations")
print( line )
# Plethora of built-in arithmetic functions are provided in Numpy.

print("Operations on single array")
a = np.array( [1,2,5,3] )

# The arithmetic operation is added to every element.
print( a+1 )  # 1 is added to every element.
#[2 3 6 4]
print( a-3 )  # 3 is subtracted to every element.
#[-2 -1  2  0]
print( a*10 )
#[10 20 50 30]

# Power of a
print( a**2 )
#[ 1  4 25  9]

# Modify the existing array
a *=2 
# Each element is doubled.
print( a )
#[ 2  4 10  6]

# Transpose of the array a
print( a.T )
#[ 2  4 10  6]
# Output is the same because of the rank is 1.(?)
# Let's check with rank=2 case.

b = np.array( [[1,2,3], [3,4,5], [9,6,0]] )
print(b)
#[[1 2 3]
# [3 4 5]
# [9 6 0]]

print(b.T)
#[[1 3 9]
# [2 4 6]
# [3 5 0]]

print("Unary operators")
# Many unary operations are provided as a method of ndarray class.
# This includes sum, min, max, etc.
# These functions can also be applied row-wise or column-wise 
#   by setting an axis parameter.

arr = np.array( [[1,5,6], [4,7,2], [3,1,9]] )
print( arr )
#[[1 5 6]
# [4 7 2]
# [3 1 9]]

# Max for the matrix
print( arr.max() )
# 9

# Row-wise Max            # GREP
print( arr.max(axis=1) )  # GREP: This is not intuitive to me.
# [6 7 9]                 # GREP

# Column-wise Max         # GREP
print( arr.max(axis=0) )  # GREP: This is not intuitive to me.
# [4 7 9]                 # GREP

print( arr.sum() )
# 38

# Column-wise sum
print( arr.sum(axis=0) )
#[ 8 13 17]

# Row-wise sum
print( arr.sum(axis=1) )
# [12 13 13]

# For each row, cumulative sum
print( arr.cumsum( axis=1) )
#[[ 1  6 12]
# [ 4 11 13]
# [ 3  4 13]]

print("Binary operators")
# These operations are applied elementwise.

a = np.array( [[1,2], [3,4]] )
print(a)
#[[1 2]
# [3 4]]

b = np.array( [[4,3], [2,1]] )
print(b)
#[[4 3]
# [2 1]]

# Elementwise sum
print(a+b)
#[[5 5]
# [5 5]]

# Elementwise multiplication
print( a*b )
#[[4 6]
# [6 4]]

# Matrix multiplication
print( a.dot(b) )
#[[ 8  5]
# [20 13]]

print("Universal functions (ufunc)")
# Mathematical functions such as sin, cos, & exp operate elementwise on an array.

a = np.array( [0,np.pi/2, np.pi] )
print( a )
# [0.         1.57079633 3.14159265]

print( np.sin(a) )
#[0.0000000e+00 1.0000000e+00 1.2246468e-16]

# I don't like this about Numpy.
# sin(pi) must be 0, not a very small number like this.
print( np.sin( np.pi ) )
# 1.2246467991473532e-16

# cos(np.pi/2) must be 0, not a very small number like this.
# What's the difference between cos( np.pi/2 - epsilon ) & cos( np.pi/2 )?
print( np.cos( np.pi/2 ) )
#6.123233995736766e-17

print( np.cos(a) )
#[ 1.000000e+00  6.123234e-17 -1.000000e+00]


print( np.exp(a) )
#[ 1.          4.81047738 23.14069263]

print( np.sqrt(a) )
#[0.         1.25331414 1.77245385]

print("4. Sorting array")
# np.sort method makes the sorting task easy for us.

a = np.array( [[1,4,2], [3,4,6], [0,-1,5]] )
print(a)
#[[ 1  4  2]
# [ 3  4  6]
# [ 0 -1  5]]

print( np.sort(a) )
#[[ 1  2  4]
# [ 3  4  6]
# [-1  0  5]]
# This is a row-wise sorting, right?

# Row-wise sorting.
# axis=1 is not necessary as a matter of fact.
# I used this option just to classify.
print( np.sort(a,axis=1) )
#[[ 1  2  4]
# [ 3  4  6]
# [-1  0  5]]

# Column-wise sorting
print( np.sort(a,axis=0) )
#[[ 0 -1  2]
# [ 1  4  5]
# [ 3  4  6]]

# Column-wise sorting AND mergesort is chosen!
print( np.sort(a,axis=0, kind='mergesort') )
#[[ 0 -1  2]
# [ 1  4  5]
# [ 3  4  6]]
# Of course, the sorted result is identical.

print( np.sort(a,axis=None) )
#[-1  0  1  2  3  4  4  5  6]
# The 2d array is flattened and then sorted!

# Structured array
dtypes = [('name','S10'),('grad_year',int),('cgpa',float)]

# Values to be put into an array
values = [('Hrithik',2009,8.5),('Ajay',2008,8.7),('Pankaj',2008,7.9),('Aakash',2009,9.0)]

# Create an array that takes in values and dtypes
arr = np.array(values, dtype=dtypes)
print(arr)
#[(b'Hrithik', 2009, 8.5) (b'Ajay', 2008, 8.7) (b'Pankaj', 2008, 7.9)
# (b'Aakash', 2009, 9. )]
# Q: What does b mean?

print( np.sort( arr,order='name') )
#[(b'Aakash', 2009, 9. ) (b'Ajay', 2008, 8.7) (b'Hrithik', 2009, 8.5)
# (b'Pankaj', 2008, 7.9)]

print( np.sort(arr, order=['grad_year','cgpa']))
#[(b'Pankaj', 2008, 7.9) (b'Ajay', 2008, 8.7) (b'Hrithik', 2009, 8.5)
# (b'Aakash', 2009, 9. )]
