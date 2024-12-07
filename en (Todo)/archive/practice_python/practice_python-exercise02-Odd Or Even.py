# -*- coding: utf-8 -*-
"""
2018-10-23 (Tue)
PRACTICE PYTHON, https://www.practicepython.org/

Exercise 2. Odd or Even
https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. 
Hint: how does an even/odd number react differently when divided by 2?

Discussion
Concepts for this week:
- Modular arithmetic (the modulus operator)
- Conditionals (if statements)
- Checking equality

Solution
https://www.practicepython.org/solution/2014/02/15/02-odd-or-even-solutions.html
"""

# Simply version
number = input("Enter an integer number:")

if int( number ) % 2 == 0:
    print("You entered an even number.")
else:
    print("You entered an odd number.")

# Advanced version
import sys

number = input("Enter an integer number:")

message = "You entered " + number + " which is an "
if int( number ) % 2 == 0:
    answer = "even"
else:
    answer = "odd"

message = message + answer + " number."
sys.stdout.write( message )