#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS231n Convolutional Neural Networks for Visual Recognition
http://cs231n.github.io/

Python Numpy Tutorial
http://cs231n.github.io/python-numpy-tutorial/

￣
python_numpy_tutorial-python-containers_set.py
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

print('Sets')
animals = {'cat', 'dog'}

print( 'cat' in animals )
#True

print( 'fish' in animals )
#False

animals.add('fish')
print( 'fish' in animals )
#True

print( len(animals) )
#3

animals.add('cat')
print( len(animals) )
#3

animals.remove('cat')
print( len(animals) )
#2

print('Loops')
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate( animals ):
    print('# %d: %s' % (idx+1,animal) )
# 1: dog
# 2: fish
# 3: cat

print('Set comprehensions')
from math import sqrt
nums ={ int( sqrt(x))  for x in range(30) }
print( nums )
#{0, 1, 2, 3, 4, 5}

for x in range(30):
    print( sqrt(x), int( sqrt(x) ) )
#0.0 0
#1.0 1
#1.4142135623730951 1
#1.7320508075688772 1
#2.0 2
#2.23606797749979 2
#2.449489742783178 2
#2.6457513110645907 2
#2.8284271247461903 2
#3.0 3
#3.1622776601683795 3
#3.3166247903554 3
#3.4641016151377544 3
#3.605551275463989 3
#3.7416573867739413 3
#3.872983346207417 3
#4.0 4
#4.123105625617661 4
#4.242640687119285 4
#4.358898943540674 4
#4.47213595499958 4
#4.58257569495584 4
#4.69041575982343 4
#4.795831523312719 4
#4.898979485566356 4
#5.0 5
#5.0990195135927845 5
#5.196152422706632 5
#5.291502622129181 5
#5.385164807134504 5