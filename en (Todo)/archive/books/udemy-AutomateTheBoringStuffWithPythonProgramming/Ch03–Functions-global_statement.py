# Ch03–Functions-global_statement.py
#
# https://automatetheboringstuff.com/chapter3/
# The global Statement

def spam():
    global eggs
    eggs = 'Inside the function'
    
eggs = 'Outside the function'
spam()
print(eggs)
#Inside the function
