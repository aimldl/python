#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS231n Convolutional Neural Networks for Visual Recognition
http://cs231n.github.io/

Python Numpy Tutorial
http://cs231n.github.io/python-numpy-tutorial/

matplotlib
https://matplotlib.org/

￣
We will highlight some parts of SciPy that you might find useful for this class.

python_numpy_tutorial-matplotlib-subplots.py
2019-07-03 (Wed)
"""
# Python Numpy Tutorial > Matplotlib > Subplots
#   Matplotlib is a plotting library similar to that of MATLAB.
#
# Read more about:
#     subplot or matplotlib.pyplot.subplot(*args, **kwargs)
#     https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplot

import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on a sine curve.
x     = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin( x )
y_cos = np.cos( x )

# Set up a subplot grid
# Height 2, width 1, 1st subplot is active.
plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.title('Sine')

# Height 2, width 1, 2nd subplot is active.
plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('Cosine')

plt.show()