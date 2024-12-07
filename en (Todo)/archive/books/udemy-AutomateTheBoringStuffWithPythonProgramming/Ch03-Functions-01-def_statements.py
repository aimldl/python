# Ch03-Functions-01-def_statements.py
#
# https://automatetheboringstuff.com/chapter3/
# Functions: Lesson 9 - def Statements, arguments, and the None value

# Simple Hello function with a def statement
def Hello():
    print('Howdy!')
    print('Hello there.')

print('First Hello()')
Hello()

print('Second Hello()')
Hello()

# def Statements with Parameters
def Hello(name):
    print('Hello, '+name)

Hello('Alice')
Hello('Bob')
