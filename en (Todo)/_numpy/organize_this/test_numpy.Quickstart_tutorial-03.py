"""
test_numpy.Quickstart_tutorial-03.py

* References
  Quickstart tutorial
    https://docs.scipy.org/doc/numpy/user/quickstart.html

TODO: Start from
A frequent error consists in calling array with multiple numeric 
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