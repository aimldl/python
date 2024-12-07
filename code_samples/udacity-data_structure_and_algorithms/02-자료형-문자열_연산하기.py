# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 07:43:48 2019

@author: aimldl
"""

# Concatenation
head = "Python"
tail = " is fun!"
print( head + tail)

#
a = "python"
print( a * 2 )

# 문자열 곱하기 응용
# Multistring

print("=" * 50 )
print("My program")
print("=" * 50 )

# 문자열 인덱싱 Indexing
a = "Life is too short. You need Python"
print( a[0] )  # 파이썬은 0부터 센다.
print( a[3] )
print( a[12] )
print( a[-1] )  # 문자열 제일 뒤 문자
print( a[-2] )  # 뒤에서 2번째 문자
print( a[-5] )  # 뒤에서 5번째 문자

# 문자열 슬라이싱 Slicing
a = "Life is too short. You need Python"
b = a[0] + a[1] + a[2] + a[3]
print( b )
# Better way
print( a[0:4] )
print( a[0:3] )
print( a[0:5] )
print( a[0:2] )
print( a[5:7] )
print( a[12:17] )
print( a[19:] )

