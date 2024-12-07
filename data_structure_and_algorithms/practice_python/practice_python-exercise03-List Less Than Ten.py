# -*- coding: utf-8 -*-
"""
2018-10-23 (Tue)
PRACTICE PYTHON, https://www.practicepython.org/

Exercise 3. List Less Than Ten
https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are 
less than 5.

Extras:
1. Instead of printing the elements one by one, make a new list that has all 
   the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements 
  from the original list a that are smaller than that number given by the user.

Solution
https://www.practicepython.org/solution/2014/02/26/03-list-less-than-ten-solutions.html
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Numbers less than 5 in a list of ", a)
for element in a:
    if (element < 5):
        print( element )
        
# Extra 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Numbers less than 5 in a list of ", a)
list_new =[]
for element in a:
    if (element < 5):
        list_new.append(element)

print("The new list:", list_new)

# Extra 2
#   list_new.append( if (element <5) [for element in a] )
print("Extra 2: write in one line")
list_oneline = list( str(x) for x in a if x < 5 )
print( list_oneline )

# Extra 3
threshold = input("Enter a number:")

import sys

message = "Numbers less than " + threshold + " will be printed from list " + str(a) +"\n"

sys.stdout.write( message )

threshold_int = int(threshold)
list_threshold = []
for element in a:
    if (element < threshold_int):
        list_threshold.append( element )

print("List with threshold", threshold_int, "is", list_threshold)

# Extra 1
#How to append a list
#list_new =[]
#list_new.append(x)
#
# Extra 2
#   list_new.append( if (element <5) [for element in a] )
#
# Reference code from
#   https://stackoverflow.com/questions/1545050/python-one-line-for-expression
#
#>>> x = [1, 2, 3, 4, 5]
#>>> y = [2*a for a in x if a % 2 == 1]
#>>> print(y)
#[2, 6, 10]   
#
# Extra 3
# TypeError: must be str, not list
#   message = "Numbers less than " + threshold + " will be printed from list " + a
# Fix
#   message = "Numbers less than " + threshold + " will be printed from list " + str(a) +"\n"
# Result
#   Numbers less than 14 will be printed from list [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]