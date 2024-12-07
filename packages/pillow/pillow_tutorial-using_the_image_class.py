#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pillow_tutorial-using_the_image_class.py

Pillow Docs > Handbook > Tutorial > Using the Image class
  Pillow 6.0.0
  https://pypi.org/project/Pillow/

  Handbook  
  https://pillow.readthedocs.io/en/latest/handbook/index.html

  Tutorial > Using the Image class
  https://pillow.readthedocs.io/en/latest/handbook/tutorial.html
---  
Pillow is the friendly PIL fork.
PIL stands for Python Imaging Library.

Installation
  $ sudo pip3 install Pillow

"""
from PIL import Image

im = Image.open("surfing_couple.jpg")
print( im.format, im.size, im.mode )
#JPEG (2048, 2048) RGB
im.show()

# The standard version of show() is not very efficient, 
#   since it saves the image to a temporary file and 
#   calls a utility to display the image.
# If you don’t have an appropriate utility installed, it won’t even work.
# When it does work though, it is very handy for debugging and tests.

# Simple geometry transforms
out = im.resize( (128,128) )
print( out.format, out.size, out.mode )
# None (128, 128) RGB
