# Ch03-Functions-03-None_value.py
#
# https://automatetheboringstuff.com/chapter3/
# Functions: Lesson 9 - def Statements, arguments, and the None value
#
# Summary
#   None represents the absence of a value like nullor undefined in other 
# programming languages. It must start with a capital N like the Boolean True
# and False values. 

# The None Value
variable = print('Hello!')

if None == variable:
    print('True')
else:
    print('False')

# Behind the scenes, Python adds return None to the end of any function
# definition with no return statement similar to how a while or for loop 
# implicitly ends with a continue statement.
# Also, if a return statement is used without a value, that is just the return 
# keyword by itself,then None is returned.