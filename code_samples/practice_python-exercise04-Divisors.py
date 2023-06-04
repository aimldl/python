# -*- coding: utf-8 -*-
"""
2018-10-23 (Tue)
PRACTICE PYTHON, https://www.practicepython.org/

Exercise 4. Divisors
https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

Create a program that asks the user for a number and then prints out a list of 
all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into 
another number. For example, 13 is a divisor of 26 because 26 / 13 has no 
remainder.)

Solution
https://www.practicepython.org/solution/2014/03/05/04-divisors-solutions.html
"""

number = input("Enter a number:")
number_int = int(number)

itr = number_int
list_divisors = []
while itr > 0:
    divisor = number_int % itr
#   print( "itr =", itr, "divisor =", divisor )
    if divisor == 0.0:
        list_divisors.append( itr )
    itr = itr -1

print("Divisors are", list_divisors)

