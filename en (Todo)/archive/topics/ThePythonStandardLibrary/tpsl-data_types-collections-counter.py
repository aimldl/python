# -*- coding: utf-8 -*-
"""
tpsl-data_types-collections-counter.py

collections — Container datatypes
https://docs.python.org/3.7/library/collections.html#module-collections

## Containers

### Python's general purpose built-in containers
  * dict
  * list
  * set
  * tuple
### Specialized container datatypes
  * namedtuple()
  * deque
  * ChainMap
  * Counter
  * OrderedDict
  * defaultdict
  * UserDict
  * UserList
  * UserString
"""
"""
#### Counter
https://docs.python.org/3.7/library/collections.html#collections.Counter

##### class collections.Counter( [iterable-or-mapping] )
A Counter is a dict subclass for counting hashable objects.
It is a collection where elements are stored as dictionary keys
  and their counts are stored as dictionary values.
Counts are allowed to be any integer value including zero or negative counts.
The Counter class is similar to bags or multisets in other languages.

See also:
[TODO: I just copied and pasted below. So interpret it by myself.]
Bag class in Smalltalk.
Wikipedia entry for Multisets.
C++ multisets tutorial with examples.
For mathematical operations on multisets and their use cases, see Knuth, Donald. The Art of Computer Programming Volume II, Section 4.6.3, Exercise 19.
To enumerate all distinct multisets of a given size over a given set of elements, see itertools.combinations_with_replacement():
map(Counter, combinations_with_replacement('ABC', 2)) # --> AA AB AC BB BC CC
"""

#%%
from collections import Counter

# Elemtns are counted from an iterable 
#   or initialized from another mapping ( or counter).
c = Counter()                     # empty counter
c = Counter('gallahad')           # iterable
c = Counter({'red':4, 'blue':2})  # mapping
c = Counter(cats=4, dogs=8)       # keyword args

# Counter objects have a dictionary interface
#   except that they return a zero count for missing items
#   instead of raising a KeyError.

c = Counter( ['eggs','ham'])
c['bacon']
# 0

#%%##################
# Removing an entry #
#####################
# Setting a count to zero doesn't remove an element from a counter.
c['sausage'] = 0
c
# Counter({'eggs': 1, 'ham': 1, 'sausage': 0})

# Use del to remove it entirely.
del c['sausage']
c
# Counter({'eggs': 1, 'ham': 1})

#%%###########
# elements() #
##############
# Return an iterator over elements
#   repeating each as many times as its count.
# The order is arbitrary.
# An element with a count less than one will be ignored.

c = Counter(a=4, b=2, c=0, d=-2)
c
# Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})
c.elements()
#<itertools.chain at 0x152ebe79240>
sorted( c.elements() )
# ['a', 'a', 'a', 'a', 'b', 'b']

#%%##################################################
# Commong patterns for working with Counter objects #
#####################################################
c.values()
# dict_values([4, 2, 0, -2])

# total of all counts
sum( c.values() )
# 4

# list unique elements
list(c)
# ['a', 'b', 'c', 'd']

# Convert to a set
set(c)
# {'a', 'b', 'c', 'd'}

# Convert to a regular dictionary
dict(c)
# {'a': 4, 'b': 2, 'c': 0, 'd': -2}

# Convert to a list of (elem,cnt) pairs
c.items()
# dict_items([('a', 4), ('b', 2), ('c', 0), ('d', -2)])

# reset all counts
c.clear()
c
#

# Note: there's no example in the tutorial,
#         but don't erase the following two lines.
# Convert from a list of (elem, cnt) pairs
# Counter( dict( list_of_pairs) )

#%%##############
# most_common() #
#################
# Return a list of the n most common elements
#   and their count from the most common to the least.
# The order is arbitrary.

Counter('abracadabra').most_common(3)
# [('a', 5), ('b', 2), ('r', 2)]

# If n is ommitted or None,
#   it returns all elements in the counter.
Counter('abracadabra').most_common(n=None)
# [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]

Counter('abracadabra').most_common()
# [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]

#%%########################
# n least common elements #
###########################
# most_common()[:-n-1:-1]
# When n=5, most_common()[:-6:-1]
Counter('abracadabra').most_common()[:-6:-1]
# [('d', 1), ('c', 1), ('r', 2), ('b', 2), ('a', 5)]

#%%##################################
# subtract( [iterable-or-mapping] ) #
#####################################
# Elements are subtracted
#   from an iterable
#   or from another mapping
#   or counter.
#
# Like dict.update() but subtracts counts instead of replacing them.
# Both inputs and outpus may be zero or negative.

c = Counter(a=4, b=2, c=0, d=-2)
c
# Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})
d = Counter(a=1, b=2, c=3, d=4)
d
# Counter({'a': 1, 'b': 2, 'c': 3, 'd': 4})
c.subtract(d)
c
# Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

#%%########################
# Mathematical operations #
###########################
# Counter objects are combined to produce multisets
#   (counters that have counts greater than zero)

#%%#######################
# Addition & Subtraction #
##########################
# Addition combines counters by adding the counts of corresponding elements
c = Counter( a=3, b=1)
d = Counter(a=1, b=2)
c+d
# Counter({'a': 4, 'b': 3})

# Subtraction combines counters by subtracting the counts of corresponding elements
c = Counter( a=3, b=1)
d = Counter(a=1, b=2)
c-d
# Counter({'a': 2})

# Another example for subtraction
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c-d
# Counter({'a': 3})

#%%###########################################################
# Note: the results for c-d and c.subtract(d) are different! #
##############################################################

#%%#####################
# Intersection & Union #
########################
# Intersection returns the minimum corresponding counts.
c = Counter( a=3, b=1)
d = Counter(a=1, b=2)

c & d
# Counter({'a': 1, 'b': 1})

# Union returns the maximum corresponding counts.
c | d
# Counter({'a': 3, 'b': 2})

#%%#############################
# Unary Addition & Subtraction #
################################
# +c removes zero and negative counts
c = Counter(a=2, b=-4)
+c
# Counter({'a': 2})
-c
# Counter({'b': 4})

#%%####################
# fromkeys( iterable) #
#######################
# This class method is not implemented for Counter objects.

#%%################################
# update( [iterable-or-mapping] ) #
###################################
#Elements are counted from an iterable or added-in from another mapping (or counter).
#Like dict.update() but adds counts instead of replacing them.
#Also, the iterable is expected to be a sequence of elements, 
#  not a sequence of (key, value) pairs.
