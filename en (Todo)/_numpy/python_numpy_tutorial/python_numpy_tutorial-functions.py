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
# Python Numpy Tutorial > Functions

def sign(x):
    if x>0:
        return 'positive'
    elif x <0:
        return 'negative'
    else:
        return 'zero'
    
for x in [-1,0,1]:
    print( sign(x) )
#   negative
#   zeroｖ
#   positive
    
def hello(name, loud=False):
    if loud:
        print('HELLO, %s!' %name.upper())
    else:
        print('HELLO, %s!' %name)

hello('Bob')
#HELLO, Bob!

hello('Fred',loud=True)
#HELLO, FRED!