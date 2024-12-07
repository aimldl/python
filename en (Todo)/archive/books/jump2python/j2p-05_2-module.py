#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
p.212
05-2.모듈
@author: aimldl
"""
# mod1.py
def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print("Different types!")
        return
    else:
        result = sum(a,b)
        return result
    
print( safe_sum('a',1) )
print( safe_sum(1,4) )
print( sum(10,10.4) )
