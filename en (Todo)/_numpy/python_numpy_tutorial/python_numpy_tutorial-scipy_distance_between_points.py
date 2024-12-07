#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS231n Convolutional Neural Networks for Visual Recognition
http://cs231n.github.io/

Python Numpy Tutorial
http://cs231n.github.io/python-numpy-tutorial/

Numpy Reference
https://docs.scipy.org/doc/numpy/reference/

SciPy
https://docs.scipy.org/doc/scipy/reference/index.html

￣
We will highlight some parts of SciPy that you might find useful for this class.

python_numpy_tutorial-scipy_distance_between_points.py
2019-07-03 (Wed)
"""
# Python Numpy Tutorial > SciPy > Distance between points
#   SciPy defines some useful functions for 
#     computing distances between sets of points.
#   scipy.spatial.distance.pdist
#     computes the distance between all pairs of points in a given set.
#   A similar function scipy.spatial.distance.cdist
#     computes the distance between all pairs of points across two sets of points.
#
# Read more about:
#     scipy.spatial.distance.pdist
#     https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html
#    
#     scipy.spatial.distance.cdist
#     https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html
#
# Python Numpy Tutorial > SciPy > MATLAB files
#   The functions scipy.io.loadmat & scipy.io.savemat allow you to
#     read and write MATLAB files.
# Read more about:
#     Input and output (scipy.io)
#     https://docs.scipy.org/doc/scipy/reference/io.html

import numpy as np
from scipy.spatial.distance import pdist, squareform

x = np.array( [[0,1],[1,0],[2,0]] )
print(x)
#[[0 1]
# [1 0]
# [2 0]]

print( pdist(x, 'euclidean') )
# [1.41421356 2.23606798 1.        ]

d = squareform( pdist(x, 'euclidean') )
print( d )
#[[0.         1.41421356 2.23606798]
# [1.41421356 0.         1.        ]
# [2.23606798 1.         0.        ]]