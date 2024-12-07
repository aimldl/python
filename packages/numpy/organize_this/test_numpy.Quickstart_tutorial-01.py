"""
test_numpy.Quickstart_tutorial-01.py

* References
  Quickstart tutorial
    https://docs.scipy.org/doc/numpy/user/quickstart.html

An example
"""

import numpy as np

a = np.arange(15).reshape( 3, 5 )

"""
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.ndim
2
>>> a.dtype.name
'int64'
>>> a.size
15
>>> type(a)
<class 'numpy.ndarray'>
"""

b = np.array( [6,7,8] )

"""
>>> b
array([6, 7, 8])
>>> type( b) 
<class 'numpy.ndarray'>
"""