#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
multithreading_in_python-3.py

Consider the program below to understand the concept of race condition:

    A race condition occurs when two or more threads can access shared data 
    and they try to change it at the same time. As a result, the values of 
    variables may be unpredictable and vary depending on the timings of 
    context switches of the processes.

Multithreading in Python | Set 2 (Synchronization)
https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/
"""

import threading 

# global variable x 
x = 0
  
def increment(): 
    """ 
    function to increment global variable x 
    """
    global x 
    x += 1
  
def thread_task(): 
    """ 
    task for thread 
    calls increment function 100000 times. 
    """
    for _ in range(100000): 
        increment() 
  
def main_task(): 
    global x 
    # setting global variable x as 0 
    x = 0
  
    # creating threads 
    t1 = threading.Thread(target=thread_task) 
    t2 = threading.Thread(target=thread_task) 
  
    # start threads 
    t1.start() 
    t2.start() 
  
    # wait until threads finish their job 
    t1.join() 
    t2.join() 
  
if __name__ == "__main__": 
    for i in range(10): 
        main_task() 
        print("Iteration {0}: x = {1}".format(i,x))

'''
First run
Iteration 0: x = 200000
Iteration 1: x = 200000
Iteration 2: x = 200000
Iteration 3: x = 200000
Iteration 4: x = 200000
Iteration 5: x = 200000
Iteration 6: x = 200000
Iteration 7: x = 200000
Iteration 8: x = 200000
Iteration 9: x = 200000
'''

'''
Second run
Iteration 0: x = 161556
Iteration 1: x = 200000
Iteration 2: x = 200000
Iteration 3: x = 200000
Iteration 4: x = 200000
Iteration 5: x = 200000
Iteration 6: x = 200000
Iteration 7: x = 200000
Iteration 8: x = 138571
Iteration 9: x = 200000
'''