#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python_numpy_tutorial-scipy_image_operations_imageio.py
TODO: Fix the following error and make this code work.

    img_tinted = Image.resize( (300,300), img_tinted )
AttributeError: module 'PIL.Image' has no attribute 'resize'

This Python script is an attempt to change the deprecated scipy.misc
to imageio and PIL (Python Imaging Library). But there's an error and
I stopped working on this code.

When I have enough free time, I may work on this, but currently, scipy.mics works.

2019-07-03 (Wed)
"""

#elif python_package == 'PIL':  # Python Imaging Library
#    from PIL import Image
#    from matplotlib.pyplot import imshow
#    
#    img = Image.open('assets/cat.jpg')
#    print( img.size)
#    # img.dtype
#    # print( img.dtype, img.size)
#    # AttributeError: 'JpegImageFile' object has no attribute 'dtype'
#    imshow( img )
#    
#    img_tinted = img * [1,0.95,0.9]

from imageio import imread, imsave
from PIL import Image
#from scipy.misc import imresize
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
imshow( img_tinted )
# Clipping input data to the valid range for imshow with RGB data 
#   ([0..1] for floats or [0..255] for integers).

# TODO: This doesn't work as it should be.
#       I may change the following line with Pillow, but I'll stop here.
#       When I have time, come back and fix this.
#       Processing individual bands
#       https://pillow.readthedocs.io/en/latest/handbook/tutorial.html
#       split the image into individual bands
#        source = im.split()
#        
#        R, G, B = 0, 1, 2
#        
#        # select regions where red is less than 100
#        mask = source[R].point(lambda i: i < 100 and 255)
#        
#        # process the green band
#        out = source[G].point(lambda i: i * 0.7)
#        
#        # paste the processed band back, but only where red was < 100
#        source[G].paste(out, None, mask)
#        
#        # build a new multiband image
#        im = Image.merge(im.mode, source)
# Resize the tinted image to be 300x300 pixels
img_tinted = Image.resize( (300,300), img_tinted )

# Write the tinted image back to disk
imsave('cat_tinted_by_imageio.jpg', img_tinted)  # AIMLDL: directory assets is removed.
imshow( img_tinted )