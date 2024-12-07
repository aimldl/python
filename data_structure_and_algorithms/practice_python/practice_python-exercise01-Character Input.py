# -*- coding: utf-8 -*-
"""
PRACTICE PYTHON, https://www.practicepython.org/

Exercise 1. Character Input
https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Create a program that asks the user to enter their name and their age. Print 
out a message addressed to them that tells them the year that they will turn 
100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and 
   printing out that many copies of the previous message.
   (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. 
   (Hint: the string "\n is the same as pressing the ENTER button)

Solution
https://www.practicepython.org/solution/2014/02/05/01-character-input-solutions.html
"""

# Exercise 1
#name = input("What is your name?")
#age = input("What is your age? Please enter a number. For example, 20 for twenty.")
#year = 100 - int(age)  + 2018
#print(name, ", you'll become 100 years old in", year  )

# Extras 1
#name = input("What is your name?")
#age = input("What is your age? Please enter a number. For example, 20 for twenty.")
#year = 100 - int(age)  + 2018
#num_of_copies = input("How many times would you like to repeat the answer?")
#
#for n in range( int(num_of_copies) ):
#    print(name, ", you'll become 100 years old in", year, ".", end='')

# Extras 2
#for n in range( int(num_of_copies) ):
#    print(name, ", you'll become 100 years old in", year, ".")
#T , you'll become 100 years old in 2075 .
#T , you'll become 100 years old in 2075 .

# The following is a code that prints without the trailing space.
# That is,
#T , you'll become 100 years old in 2075 . (Wrong)
#T, you'll become 100 years old in 2075.   (Right)

import sys

name = input("What is your name?")
age = input("What is your age? Please enter a number. For example, 20 for twenty.")
year = 100 - int(age)  + 2018
num_of_copies = input("How many times would you like to repeat the answer?")

for n in range( int(num_of_copies) ):
    message = name + ", you'll become 100 years old in " + str(year) + "."
    sys.stdout.write(message)

"""
input("message")

int(age)
TypeError: 'str' object cannot be interpreted as an integer

Python: How to Print Without Newline? (The Idiomatic Way)
https://www.afternerd.com/blog/how-to-print-without-a-newline-in-python/

Print without a new line.
print("message", end='')

sys.stdout.write(name, ", you'll become 100 years old in", year, ".")
TypeError: write() takes 2 positional arguments but 5 were given

String Concatenation and Formatting
https://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python
TypeError: must be str, not int
message = name + ", you'll become 100 years old in " + year + "."
=> message = name + ", you'll become 100 years old in " + str(year) + "."
"""