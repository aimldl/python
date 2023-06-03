#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS231n Convolutional Neural Networks for Visual Recognition
http://cs231n.github.io/

Python Numpy Tutorial
http://cs231n.github.io/python-numpy-tutorial/

Numpy Reference
https://docs.scipy.org/doc/numpy/reference/
￣
2019-07-02 (Tue)
"""
# Python Numpy Tutorial > Classes

class Greeter(object):
    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable
        
    # Instance method
    def greet(self,loud=False):
        if loud:
            print('HELLO, %s' %self.name.upper())
        else:
            print('HELLO, %s' %self.name)

g = Greeter('Fred')
g.greet()
# HELLO, Fred
g.greet(loud=True)
# HELLO, FRED