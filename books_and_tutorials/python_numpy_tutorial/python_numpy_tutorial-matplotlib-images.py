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

python_numpy_tutorial-matplotlib-images.py
2019-07-03 (Wed)
"""
# Python Numpy Tutorial > Matplotlib > Images
#   Matplotlib is a plotting library similar to that of MATLAB.
#
# Read more about:
#     matplotlib.pyplot.imshow
#     https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.imshow.html

import numpy as np
from imageio import imread
import matplotlib.pyplot as plt

img        = imread('assets/cat.jpg')
img_tinted = img * [1,0.95,0.9]

# Show the original image
plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
# Note nothing will show without np.uint8( ... )
plt.imshow( np.uint8( img_tinted) )
#plt.imshow( img_tinted )
plt.show()