# -*- coding: utf-8 -*-
"""
2018-10-25 (Thu)
PRACTICE PYTHON, https://www.practicepython.org/

Exercise 7. List Comprehensions
https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

Let’s say I give you a list saved in a variable: 
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list 
that has only the even elements of this list in it.

Solution
https://www.practicepython.org/solution/2014/03/26/07-list-comprehensions-solutions.html
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# My answer
list_new = list( x for x in a if x % 2 ==0 )
print( list_new )

# Solution
print( [ x for x in a if x % 2 ==0] )
