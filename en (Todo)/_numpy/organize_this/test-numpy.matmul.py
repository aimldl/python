# -*- coding: utf-8 -*-
"""
References
  numpy.matmul¶
    https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.matmul.html
"""

import numpy as np

# Examples

# For 2-D arrays it is the matrix product:
a = [[1,0], [0,1]]
b = [[4,1], [2,2]]
np.matmul(a,b)

# For 2-D mixed with 1-D, the result is the usual.
a = [[1,0],[0,1]]
b = [1,2]
np.matmul(a,b)
np.matmul(b,a)

# Broadcasting is conventional for stacks of arrays

a = np.arange(2*2*4).reshape((2,2,4))
"""
np.arange(2*2*4)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
np.arange(2*2*4).reshape((2,2,4))
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7]],

       [[ 8,  9, 10, 11],
        [12, 13, 14, 15]]])
"""

b = np.arange(2*2*4).reshape((2,4,2))
"""
array([[[ 0,  1],
        [ 2,  3],
        [ 4,  5],
        [ 6,  7]],

       [[ 8,  9],
        [10, 11],
        [12, 13],
        [14, 15]]])
"""

# 2x2x4 X 2x4x2
np.matmul(a,b).shape
"""(2, 2, 2)"""

np.matmul(a,b)
"""
array([[[ 28,  34],
        [ 76,  98]],

       [[428, 466],
        [604, 658]]])
"""

np.matmul(a,b)[0,1,1]
"""98"""
"""
a[0,1,:] = array([4, 5, 6, 7])
b[0,:,1] = array([1, 3, 5, 7])
* is a piece-wise multiplication?
a[0,1,:] * b[0,:,1]
array([ 4, 15, 30, 49])
"""

sum( a[0,1,:] * b[0,:,1])
"""98"""

# Vector, vector returns the scalar inner product, but neither argument is complex-conjugated:
np.matmul([2j,3j], [2j,3j])

''' (1x2) X (1x2) I don't understand this part.
'''
a = [2j,3j]
b = [2j,3j]
np.matmul(a,b)
'''(-13+0j)'''

a = [[2j,3j]]
b = [[2j,3j]]
np.matmul(a,b)
# ValueError: shapes (1,2) and (1,2) not aligned: 2 (dim 1) != 1 (dim 0)

np.matmul([1,2], 3)
'''
Traceback (most recent call last):

  File "<ipython-input-38-a054dc69a9a6>", line 1, in <module>
    np.matmul([1,2], 3)

ValueError: Scalar operands are not allowed, use '*' instead
'''