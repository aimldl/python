# -*- coding: utf-8 -*-
"""
jump2python-02_2-string_built_in_methods.py
P.59, 문자열 관련 함수들
"""

# 문자 개수 세기
a = 'hobby'
a.count('b')
# 2

a.count('bb')
# 1

a.count('oo')
# 0

# find 문자 위치 알려주기

a = 'Python is the best choice'
a.find('b')
# 14
# The first location of b

a.find('k')
# -1
# 0 means the first element,so
# -1 means it doesn't exist, not the last element.

# index 위치 알려주기
b = 'Life is too short'
b.index('t')
# 8

# b.index('k')
# ValueError: substring not found

# Q: Then what's the difference between find & index?
a.index('b')
# 14
b.find('t')
# 8 

# A: The difference is .index gives an error 
#      if the input character (or string?) doesn't exist.
# a.index('k')
# ValueError: substring not found

# join 문자열 삽입 
a = ","
a.join('abcd')
'a,b,c,d'

# upper 소문자를 대문자로 바꾸기 
a = 'hi'
a.upper()
# HI

# lower 대문자를 소문자로 바꾸기
a = 'HELLO'
a.lower()
# hello

# strip (양쪽) 공백 지우기, strip (off the spaces)
a = '   hi, there  '
a.strip()
# 'hi, there'

# lstrip 왼쪽 공백 지우기 
a = '   hi, there  '
a.lstrip()
# 'hi, there  '

# lstrip 오른쪽 공백 지우기 
a = '   hi, there  '
a.rstrip()
# '   hi, there'

# replace 문자열 바꾸기
a = 'Keep calm and carry on.'
a.replace('carry','surf')
#'Keep calm and surf on.'

# 문자열 나누기 (split)
a = "Life is too short"
print( a.split() )  # Default is to delimit with space.
#['Life', 'is', 'too', 'short']

b = "a:b:c:d"
print( b.split() )
#['a:b:c:d']

c = "a:b:c:d"
print( c.split(":") )
#['a', 'b', 'c', 'd']

###################
# Another example #
###################
a = 'Keep calm and surf on.'  # I've changed 'Life is too short'
a.split()
# ['Keep', 'calm', 'and', 'surf', 'on.']
print( a[0] )
# K

print( a.split() [0] )
# Keep

b=a.split()  # The default is space.
print( b[0] )
print( b[3],b[4] )
# surf on.


