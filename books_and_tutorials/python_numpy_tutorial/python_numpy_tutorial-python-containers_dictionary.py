#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS231n Convolutional Neural Networks for Visual Recognition
http://cs231n.github.io/

Python Numpy Tutorial
http://cs231n.github.io/python-numpy-tutorial/

￣
python_numpy_tutorial-python-containers_dictionary.py
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

print('Dictionary')

# Create a new dictionary
d = {'cat':'cute','dog':'furry'}
print( d )
#{'cat': 'cute', 'dog': 'furry'}
print( d['cat'] )
# cute

# Check if a dictionary has 'cat'.
print( 'cat' in d )
# True

# Set an entry in the dictionary.
d['fish'] = 'wet'
print( d['fish'] )
# wet
print( d )
#{'cat': 'cute', 'dog': 'furry', 'fish': 'wet'}

# Get an element with a default
print( d.get('monkey', 'N/A') )
# N/A
# because 'monkey' is not there, prints N/A

# Get an element with a default
print( d.get('fish','N/A') )
#wet
# because 'fish' is there, prints the value of it!

del d['fish']
print( d.get('fish','N/A') )
#N/A
# because 'fish' is deleted, 'fish' isn't in the list of the keys.
# So prints N/A

print('Loops')
d = {'person':2, 'cat':4, 'spider':8}
for animal in d:      # Only the key is returned
    #print( animal )
    legs = d[animal]
    print('A %s has %d legs.' %(animal, legs))
    
print('Dictionary comprehensions')
# Dictionary comprehensions are similar to list comprehensions.
# But these allow you to easily construct dictionaries.
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x**2 for x in nums if x%2 == 0}
print( even_num_to_square )
#{0: 0, 2: 4, 4: 16}