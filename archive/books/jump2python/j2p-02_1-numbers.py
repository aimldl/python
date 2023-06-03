# -*- coding: utf-8 -*-
"""
jump2python-02_1-numbers.py
jump2python-02_1-숫자형
정수   integer
실수   float
복소수 complex
8진수  octal
16진수 hex
"""

# Numbers

# Integer
a =  123
a = -178
a = 0

# Float
a = 1.2
a = -3.45

# Both E & e are fine.
a = 4.24E10
a = 4.24e-10

# Octal
#   starts from 0o
#   where 0 is a number; o is a character
a = 0o177

# Hex
#   starts from 0x
a = 0x8ff

# Complex number
#   j or J is used instead of i
a = 1+2j
b = 3-4J

print( a.real )
# 1.0

print( a.imag )
# 2.0

print( a.conjugate )
# <built-in method conjugate of complex object at 0x000002218942B870>

print( a.conjugate() )
# (1-2j)
# I don't like the fact that the convention is inconsistent.

print( abs(a) )
# 2.23606797749979
# = sqrt(1^2+2^2)

# 사칙연산 연산자
a = 3
b = 4
print( a + b )
#7
print( a - b )
#-1
print( a * b )
#12
print( a / b )
#0.75

# Note Python2 returns 0 for a/b because integer / integer = integer in Python2.
# In Python2, convert the integer b to float b by, say, a/(b*1.0).
# Python3 doesn't need to convert it. It's just automatic.

# Power 제곱
a ** b 
# 81

# Modulo연산자
#   나눗셈 후 나머지를 반
print( 7 % 4 )
# 3

# //연산자
#   나눗셈 후 소수점 아래자리를 버린다.
print( 7//4 )
# 1 
print( 7/4 )
# 1.75