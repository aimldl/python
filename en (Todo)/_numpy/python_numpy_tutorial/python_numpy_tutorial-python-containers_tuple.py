#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS231n Convolutional Neural Networks for Visual Recognition
http://cs231n.github.io/

Python Numpy Tutorial
http://cs231n.github.io/python-numpy-tutorial/

￣
python_numpy_tutorial-python-containers_tuple.py
2019-07-03 (Wed)
"""
# Python Numpy Tutorial > Python > Containers
#   Python's built-in container types:
#     lists, dictionaries, sets, and tuples.
#
#   (Python) Lists
#     a mutable ordered list of values.
#     A list is the Python equivalent of an array with useful functions.
#     A Python list is resizeable and
#                   can contain elements of different types.
#
#   Dictionaries
#     stores key-value pairs
#
#   Sets
#     an unordered collection of distinct elements.
#
#   Tuples
#     an immutable ordered list of values.
#     A tuple is similar to a list, but different in that
#       tuples can be used as keys in dictionaries and
#                          as elements of sets.
#
#   =[,,]    (Python) list ~= Dynamic array (with useful functions)
#   ={:,:,:} Dictionary    ~= Map  
#   ={,,}    Set            = Set
#   =(,)     Tuples        ~= (Python) list
#
# This example covers:
#   Lists
#     Slicing
#       A concise syntax to access sublists.
#     Loops
#       You can loop over the elements of a list.
#       The enumerate function returns the index & value.
#     List comprehensions
#       A concise way to loop through a list.
#       e.g. 3 lines of code -> 1 line of code
#
#   Dictionaries
#     (Basics)
#     Loops
#     Dictionary comprehensions
#
#   Sets
#     (Basics)
#     Loops
#       Iterating over a set has the same syntax as a list.
#       However you cannot make assumptions about the order.
#     Set comprehensions
#       Like list comprehension & dictionary comprehension,
#       constructing a set is easy with set comprehensions.
#
#   Tuple
#     (Basics)
#
# Read more about:
#   4.6.4. Lists¶
#   https://docs.python.org/3.5/library/stdtypes.html#lists
#
#   4.9. Set Types — set, frozenset¶
#   https://docs.python.org/3.5/library/stdtypes.html#set
#
#   4.10. Mapping Types — dict
#   https://docs.python.org/3.5/library/stdtypes.html#dict
#
#   5.3. Tuples and Sequences
#   https://docs.python.org/3.5/tutorial/datastructures.html#tuples-and-sequences

print('Tuples')

# Create a dictionary with tuple keys
d = { (x,x+1): x for x in range(10)}
print(d)
#{(0, 1): 0, (1, 2): 1, (2, 3): 2, (3, 4): 3, (4, 5): 4, 
# (5, 6): 5, (6, 7): 6, (7, 8): 7, (8, 9): 8, (9, 10): 9}

print( d[(1,2)] )
#1
print( d[(5,6)] )
#5

# Create a tuple
t = (5,6)
print( type(t) )
#<class 'tuple'>
print( d[t] )
#5
