#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
multithreading_in_python-1.py

In Python, the threading module provides a very simple and intuitive API 
  for spawning multiple threads in a program.
Let us consider a simple example using threading module:

Multithreading in Python | Set 1
https://www.geeksforgeeks.org/multithreading-python-set-1/
"""
# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread( target=print_square, args=(10,) ) 
    t2 = threading.Thread( target=print_cube, args=(10,) ) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 

#Square: 100
#Cube: 1000
#Done!