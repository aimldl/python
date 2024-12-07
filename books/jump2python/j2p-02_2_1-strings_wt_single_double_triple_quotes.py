# -*- coding: utf-8 -*-
"""
jump2python-02_2-strings_wt_single_double_triple_quotes.py
jump2python-02_2-문자열 자료형
"""

# Single quote ''
'Python is fun'

# Double quote ""
"Hello, world"

# Triple? with ', '''
''' This is a multi-line comments.
    Life is too short.
    You need Python.'''

# Triple? with ", """
""" This is also a multi-line comments.
    Life is too short.
    You need Python."""
    
# Why four types of comments?

# 1.문자열에 작은 따옴표 ' 포함시키기

# favorite_food_error = 'Python's favorite food is perl.'
# print( favorite_food_error )

favorite_food = "Python's favorite food is perl."
print( favorite_food )
#Python's favorite food is perl.

# 2. 문자열에 큰 따옴표 " 포함시키기

#he_saids_error = ""Python is very easy." he said"
#print( he_saids_error )
#SyntaxError: invalid syntax

he_said = '"Python is very easy." he said'
print( he_said )
# "Python is very easy." he said

# Using a back slash
# favorite_food_error can be fixed with \
favorite_food_wt_back_slash = 'Python\'s favorite food is perl.'
print( favorite_food_wt_back_slash )
#Python's favorite food is perl.

# he_saids_error can be fixed with \
he_saids_wt_back_slash = "\"Python is very easy.\" he said"
print( he_saids_wt_back_slash )
#"Python is very easy." he said

# Multiple lines in a string

# Using an escape code
multiline = "Life is too short. \nWe need surfing."
print( multiline )
#Life is too short. 
#We need surfing.

# Using triple single quotes
multiline_with_triple_single_quotes = '''Life is too short.
We need surfing.'''
print( multiline_with_triple_single_quotes )
#Life is too short.
#We need surfing.

# Using triple double quotes
multiline_with_triple_double_quotes = """Life is too short.
We need surfing.
"""
print( multiline_with_triple_double_quotes )
#Life is too short.
#We need surfing.