# Ch03-Functions-02-return_statements.py
#
# https://automatetheboringstuff.com/chapter3/
# Functions: Lesson 9 - def Statements, arguments, and the None value
#
# Changes from the original code
# - I recuded the number of if-else statements.

# Return Values and return Statements

import random

def getAnswer( answerNumber ):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    else:
        return 'Out of the answer range of 1~3'

for i in range(1,11):
    # Run this for ten times
    rand_num = random.randint(1,4)
    print('rand_num = ', rand_num)
    answer = getAnswer( rand_num )
    print( answer )
