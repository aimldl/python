# -*- coding: utf-8 -*-
"""
2018-10-25 (Thu)
PRACTICE PYTHON, https://www.practicepython.org/

Exercise 6. String Lists
https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

Ask the user for a string and print out whether this string is a palindrome or 
not. (A palindrome is a string that reads the same forwards and backwards.)

palin-drome is a paragraph that makes as much sense forwards as backwards

Solution
https://www.practicepython.org/solution/2014/03/19/06-string-lists-solutions.html
"""


input_string = input("Enter a string to check if it's palindrome:")
input_string = str( input_string )

print( "Solution without a loop" )
reversed_string = input_string[::-1]

if reversed_string == input_string:
    print(input_string, "is a palindrome.")
else:
    print(input_string, "is not a palindrome.")

print( "Solution with a loop" )
string_length = len( input_string )
index_left = 0
index_right = string_length -1
is_palindrome = True
    
while index_left < index_right:
    if input_string[index_left] == input_string[index_right]:
        index_left += 1
        index_right -= 1
        is_palindrome = True
        continue
    else:
        is_palindrome = False
        break

if is_palindrome:
    print(input_string, "is a palindrome.")
else:
    print(input_string, "is not a palindrome.")