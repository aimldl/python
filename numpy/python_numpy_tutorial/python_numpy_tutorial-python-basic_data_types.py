#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS231n Convolutional Neural Networks for Visual Recognition
http://cs231n.github.io/

Python Numpy Tutorial
http://cs231n.github.io/python-numpy-tutorial/

￣
python_numpy_tutorial-python-basic_data_types.py
2019-07-03 (Wed)
"""
# Python Numpy Tutorial > Python > Basic data types
#   Numbers
#     integers & floats work as you would expect from other languages.
#     Python doesn't have unary increment/decrement operators or x++ / x--. 
#     Complex numbers are supported 
#
#   Booleans
#     All of the logic operators are supported.
#     The operators are in English words rather than symbols.
#     For example, (A and B) (A or B) rather than (A&&B) (A||B).
#
#   Strings
#     Strings are surround by:
#      single quotes 'str'
#      double quotes "str"
#      triple quotes '''str'''
#      triple quotes """str"""
#     String objects have a bunch of useful methods.
#
# This example covers:
#   Numeric types: int, float, complex
#   booleans
#   strings
#
# Read more about:
#   4.4. Numeric Types — int, float, complex
#   https://docs.python.org/3.5/library/stdtypes.html#numeric-types-int-float-complex

print('Numbers: integers')
x = 3
print( x )
#3
print( type(x) )
#<class 'int'>
print( x+1 )    # Addition
#4
print( x-1 )    # Subtraction    
#2
print( x*2 )    # Multiplication
#6
print( x**2 )   # Exponentiation
#9
x +=1
print( x )
#4
x *= 2
print( x )
#8

print('Numbers: floats')
y = 2.5
print( type(y) )
#<class 'float'>
print(y,y+1,y*2,y**2)
#2.5 3.5 5.0 6.25

print('Booleans')
t = True
f = False
print( type(t) )
#<class 'bool'>
print( t and f )    # Logical AND
#False
print( t or f )     # Logical OR
#True
print( not t)       # Logical not
#False
print( t != f )     # Logical XOR
#True

print('Strings')
hello = 'hello'
world = "world"
print( hello )
#hello
print( len(hello) )
#5

# String concatenation
hw = hello + ', ' + world
print(hw)
#hello, world

# sprintf style string formatting
hw12 = '%s %s %d' % (hello,world,12)
print(hw12)
#hello world 12

# Methods
s = hello
print( s.capitalize() )
#Hello
print( s.upper() )
#HELLO

# Right-justing a string; padding with spaces
print( s.rjust(7) )
#  hello

# Cetering a string; padding with spaces
print( s.center(7) )
# hello 
print( s.replace('l','(ell)'))
#he(ell)(ell)o

# Strip leading and trailing whitespaces.
print('   world   '.strip() )
#world