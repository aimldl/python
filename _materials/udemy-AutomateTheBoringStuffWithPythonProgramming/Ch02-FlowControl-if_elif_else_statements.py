# Ch02-FlowControl-if_elif_else_statements.py
# This is an example for if, elif, and else statements.
#
# https://automatetheboringstuff.com/chapter2/
# Flow Control Statements: Lesson 5 - if, elif, and else

name = 'Dracula'
age = 4000

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('UNlike you, Alice is not an undead, immortal vampire.')
else:
    print('Well, I have no idea who you are, ', name)
