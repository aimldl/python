"""
test_numpy.Quickstart_tutorial-02.py

* References
  Quickstart tutorial
    https://docs.scipy.org/doc/numpy/user/quickstart.html

Array Creation
There are several ways to create arrays.

For example, you can create an array from a regular Python list or tuple using 
the array function. The type of the resulting array is deduced from the type of 
the elements in the sequences.
"""

import numpy as np

a = np.array( [2,3,4] )

"""
>>> a
array([2, 3, 4])
>>> a.dtype
dtype('int64')
>>> a.dtype.name
'int64'
"""

b = np.array( [1.2, 3.5, 5.1] )

"""
>>> b.dtype
dtype('float64')
"""