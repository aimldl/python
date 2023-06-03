#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS231n Convolutional Neural Networks for Visual Recognition
http://cs231n.github.io/

Python Numpy Tutorial
http://cs231n.github.io/python-numpy-tutorial/

￣
python_numpy_tutorial-python-containers_list.py
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

print('Lists')
xs = [3,1,2]

#
print( xs, xs[2] )
#[3, 1, 2] 2

# Negative index is from the end of the list
print( xs[-1] )
#2

# A list can have elements of different types
xs[2] = 'foo'
print( xs )
#[3, 1, 'foo']

# A method can be used to add a new element to the end of the list
xs.append('bar')
print( xs )
#[3, 1, 'foo', 'bar']

# Remove and return the last element
x = xs.pop()
print(x)
#bar
print(xs)
#[3, 1, 'foo']

print('Slicing')
nums = list( range(5) )  # GREP: 5 elements from 0, so 0:[5-1]
print( nums )
#[0, 1, 2, 3, 4]
print( nums[2:4] )  # GREP: Think of it as nums[2:3] or 2:(4-1).
#[2, 3]
print( nums[2:] )
#[2, 3, 4]
print( nums[:2] )   # GREP: Think of it as nums[:1] or :(2-1).
#[0, 1]
print( nums[:] )    # The whole list
#[0, 1, 2, 3, 4]
print( nums[:-1])
#[0, 1, 2, 3]
nums[2:4] = [8,9]   # GREP: nums[2:4] means 2:(4-1)
print( nums )
#[0, 1, 8, 9, 4]

print('Loops')
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print( animal )
#cat
#dog
#monkey
    
# If you want to accces to the index of each element 
#   within the body of a loop, use the enumerate function.

animals = ['cat', 'dog', 'monkey']
for index, animal in enumerate(animals):
    print('# %d: %s' % (index+1, animal) )
# 1: cat
# 2: dog
# 3: monkey
    
print('List comprehensions')

# Compute square numbers.
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append( x**2 )
print( squares )
# [0, 1, 4, 9, 16]

# Make the above code simpler with a list comprehension.
nums = [0, 1, 2, 3, 4]
squares = [ x**2 for x in nums ]
print( squares )
# [0, 1, 4, 9, 16]

# A list comprehension can contain conditions.
num = [0, 1, 2, 3, 4]
even_squares = [ x**2 for x in num if x%2 == 0 ]
print( even_squares )
# [0, 4, 16]