#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
multithreading_in_python-2.py

Consider the python program given below 
  in which we print thread name and corresponding process for each task:

Multithreading in Python | Set 1
https://www.geeksforgeeks.org/multithreading-python-set-1/
"""

# Python program to illustrate the concept 
# of threading 
import threading 
import os 
  
def task1(): 
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name)) 
    print("ID of process running task 1: {}".format(os.getpid())) 
  
def task2(): 
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name)) 
    print("ID of process running task 2: {}".format(os.getpid())) 
  
if __name__ == "__main__": 
  
    # print ID of current process 
    print("ID of process running main program: {}".format(os.getpid())) 
  
    # print name of main thread 
    print("Main thread name: {}".format(threading.main_thread().name)) 
  
    # creating threads 
    t1 = threading.Thread(target=task1, name='t1') 
    t2 = threading.Thread(target=task2, name='t2')   
  
    # starting threads 
    t1.start() 
    t2.start() 
  
    # wait until all threads finish 
    t1.join() 
    t2.join() 

'''
ID of process running main program: 16897
Main thread name: MainThread
Task 1 assigned to thread: t1
ID of process running task 1: 16897
Task 2 assigned to thread: t2
ID of process running task 2: 16897
'''