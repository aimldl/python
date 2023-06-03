# Ch02-FlowControl-while_break_continue_statements.py
# This is an example for while, break, continue statements.
#
# https://automatetheboringstuff.com/chapter2/
# Flow Control Statements: Lesson 6 - while Loops, break, and continue
#
# I changed the original code slightly.
 
count = 0
while True:
    print('What is your name?')
    name = input()
    if name != 'Joe':
        if count > 2:
            print('Hint: The name should be Joe.')
        count = count + 1
        continue

    print('Hi, Joe. What is the password?')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')
