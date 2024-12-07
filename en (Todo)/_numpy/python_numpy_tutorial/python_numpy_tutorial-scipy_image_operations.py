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

python_numpy_tutorial-scipy_image_operations.py
2019-07-03 (Wed)
"""
# Python Numpy Tutorial > SciPy > Image Operations
#   SciPy provides some basic functions to work with images.
#
# This examples tints & resizes the original image.
# tint
#   Verb[VN] 1.[타동사] [주로 수동태로] ~ sth (with sth) (약간의) 색깔을 넣다[색조를 더하다]
#   2.[타동사] (머리를) 염색하다
# This example covers:
#   reading in an image 'imread'
#   image tinting by multiplying scalar values 'img * [1 0.95 0.9]'
#   resizing the image 'imresize'
#   saving the image 'imsave'
#
#   scipy.misc vs. PIL vs. imageio
#
# Read more about:
#     matplotlib.pyplot.imshow
#     https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.imshow.html

# runfile('/home/aimldl/Dropbox/sw-now/python/python_numpy_tutorial/python_numpy_tutorial-scipy_image_operations.py',
#    wdir='/home/aimldl/Dropbox/sw-now/python/python_numpy_tutorial')

# runfile('/home/aimldl/Dropbox/sw-now/python/python_numpy_tutorial/python_numpy_tutorial-scipy_image_operations.py', 
#   wdir='/home/aimldl/Dropbox/sw-now/python/python_numpy_tutorial')

from scipy.misc import imread, imsave
from scipy.misc import imresize
from matplotlib.pyplot import imshow

# Read an JPEG image into a numpy array
img = imread('cat.jpg')  # AIMLDL: assets/cat.jpg is changed to cat.jpg
print( img.dtype,img.shape )
# uint8 (400, 248, 3)

#img = imread('sample_images/surfing-01.jpg')
#print( img.dtype,img.shape )
#uint8 (2048, 2048, 3)

imshow( img )

# The image is tinted by scaling each of the color channels by a different scalar constant. 
# For examples, when [1, 0.95, 0.9] is multiplied by numpy broadcasting:
#   the red channel is unchanged.
#   the green channel is multiplied by 0.95
#   the blue channel is multiplied by 0.9.
# If [1,1,1] is multiplied, it's the same as the original image.

img_tinted = img * [1,0.95,0.9]
#img_tinted = img * [1,0.99,0.98]
#imshow( img_tinted )  # Note nothing will show without np.uint8( ... )
imshow( np.uint8 (img_tinted) )
# Clipping input data to the valid range for imshow with RGB data 
#   ([0..1] for floats or [0..255] for integers).

# Resize the tinted image to be 300x300 pixels
img_tinted = imresize( img_tinted, (300,300) )

# Write the tinted image back to disk
imsave('cat_tinted.jpg', img_tinted)  # AIMLDL: directory assets is removed.
imshow( img_tinted )

"""
# Note
## DeprecationWarning
from scipy.misc import imread, imsave, imresize
img = imread('image_filename.jpg')
  will cause the following warning message:
    DeprecationWarning: `imread` is deprecated!
    `imread` is deprecated in SciPy 1.0.0, and will be removed in 1.2.0.
    Use ``imageio.imread`` instead.

## How to switch from scipy to imageio
### Step 1. Install imageio
            by typing '$ sudo pip3 install imageio'. Otherwise you'll see:
            Import Error: No module named 'imageIO'
          
### $ sudo pip3 install imageio
    [sudo] password for aimldl: 
    Collecting imageio
    Downloading https://files.pythonhosted.org/packages/af/0a/943c965d372dae0b1f1482677d29030ab834351a61a9a632fd62f27f1523/imageio-2.5.0-py3-none-any.whl (3.3MB)
    100% |████████████████████████████████| 3.3MB 478kB/s 
    Requirement already satisfied: numpy in /home/aimldl/.local/lib/python3.6/site-packages (from imageio)
    Requirement already satisfied: pillow in /home/aimldl/.local/lib/python3.6/site-packages (from imageio)
    Installing collected packages: imageio
    Successfully installed imageio-2.5.0
    $
    
### Step 2. Import imageio instead of scipy     
              from imageio import imread
              img = imread('image_filename.jpg')

## DeprecationWarning: `imresize` is deprecated!
`imresize` is deprecated in SciPy 1.0.0, and will be removed in 1.3.0.
Use Pillow instead
"""