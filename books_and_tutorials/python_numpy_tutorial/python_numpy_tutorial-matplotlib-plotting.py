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

python_numpy_tutorial-matplotlib-plotting.py
2019-07-03 (Wed)
"""
# Python Numpy Tutorial > Matplotlib > Plotting
#   Matplotlib is a plotting library similar to that of MATLAB.
#
# Read more about:
#     plot or matplotlib.pyplot.plot(*args, **kwargs)
#     https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

import numpy as np
import matplotlib.pyplot as plt

# Example 1
# Compute the x and y coordinates for points on a sine curve.
x = np.arange(0,3*np.pi,0.1)
y = np.sin( x )

# Plot the points using matplotlib
plt.plot(x,y)
# You must call plt.show() to make graphics appear.
plt.show()

# Example 2
# Compute the x and y coordinates for points on sine and cosine curves.
x     = np.arange(0,3*np.pi,0.1)
y_sin = np.sin( x )
y_cos = np.cos( x )

# Plot the points using matplotlib
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend( ['Sine','Cosine'] )

# You must call plt.show() to make graphics appear.
plt.show()