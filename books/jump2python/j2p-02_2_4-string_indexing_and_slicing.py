# -*- coding: utf-8 -*-
"""
jump2python-02_2_4-string_indexing_and_slicing.py
P.47, 문자열 인덱싱과 슬라이싱
인덱싱 = 가리킨다
슬라이싱 = 무언인가를 잘라낸다.
"""

#####################
# 문자열 인덱싱이란? #
#####################
#   Python은 0부터 숫자를 센다.
a = "Life is too short. You need Python"
print( a[3] )
# e

# 문자열 인덱싱 활용하기
print( a[0], a[12], a[-1] )
# L s n
# -1는 뒤에서부터 세는 경우이다.

print( a[0], a[-0])
# L L
# 그러므로 0과 -0은 동일한 결과를 보여준다.

# a[-2] 뒤에서 두번째 문자
# a[-5] 뒤에서 다섯번째 문자
print( a[-2], a[-5])
# o y

#######################
# 문자열 슬라이싱이란? #
#######################
a = "Life is too short. You need Python"
b = a[0] + a[1] + a[2] + a[3]
print( b )
# Life

# 슬라이싱으로 동일한 결과를 얻을 수 있다.
# 처음인 0부터 (4-1)까지
print( a[0:4] )
# Life

print( a[0:3] )
# Lif

##########################
# 문자열 슬라이싱하는 방법 #
##########################
print( a[0:5] )
# 'Life '

# 슬라이싱의 시작을 0이 아닌 것에서 시작할 수 있다.

print( a[0:2] )
# Li
print( a[5:7] )
# is
print( a[12:17] )
#short

# : 뒤의 숫자가 없으면 끝까지...
print( a[19:] )
# You need Python

# : 앞의 숫자가 없으면 앞에서부터...
print( a[:17] )
# Life is too short

# : 앞뒤가 없으면 전체...
print( a[:] )
#Life is too short. You need Python

# 슬라이싱에서도 -기호를 쓸 수 있다.
print( a[19:-7] )
# You need

#############################
# 슬라이싱으로 문자열 나누기 #
#############################
print( a[19:-7] )
a = '20010331Rainy'
date = a[:8]
weather = a[8:]
print( date )
# 20010331
print( weather )
# Rainy

year = a[:4]
day = a[4:8]
weather = a[8:]

print( year )
# 2001
print( day )
# 0331
print( weather )
# Rainy

############################################
# Pithon이라는 문자열을 Python으로 바꾸려면? #
############################################
# string = immutable data type
a = 'Pithon'
print( a[1] )
# a[1] = 'y'
# 위와 같이 실행하면 아래의 에러가 뜬다.
#   TypeError: 'str' object does not support item assignment
# 왜냐하면 문자열의 요소값은 변경하지 못 하기 때문이다.
# 다른 표현을 쓰자면 string은 immitable한 자료형이다.
# 그러므로...

b = a[0]+ 'y' + a[2:]
print( b )
# Python