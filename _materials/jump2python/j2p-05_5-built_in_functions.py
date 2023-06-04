# -*- coding: utf-8 -*-
"""
j2p-05_5-built_in_functions.py

p.234, 05-5. 내장 함수

# The following list is the full list of built-in functions in Python Docs.
This script covers a part of the full list.

Built-in Functions
  https://docs.python.org/3/library/functions.html

__import__()
abs()
all()
any()
ascii()
bin()
bool()
breakpoint()
bytearray()
bytes()
callable()
chr()
classmethod()
compile()
complex()
delattr()
dict()
dir()
divmod()
enumerate()
eval()
exec()
filter()
float()
format()
frozenset()
getattr()
globals()
hasattr()
hash()
help()
hex()
id()
input()
int()
isinstance()
issubclass()
iter()
len()
list()
locals()
map()
max()
memoryview()
min()
next()
object()
oct()
open()
ord()
pow()
print()
property()
range()
repr()
reversed()
round()
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
tuple()
type()
vars()
zip()

"""
#%% abs
print( abs(3), abs(-3), abs(1.2) )
# 3 3 1.2

#%% all
#   returns True when all elements are True.
#   returns False if any element has False.

all( [1,1,1,1] )
# True

all( [0,1,1,1] )
# False

all( [1,2,3] )
# True

all( [1,2,3,0] )
# False

#%% any
#   returns True when any elements are True.
#   returns False only when all elements are False.

any( [1,1,1,1] )
# True

any( [0,1,1,1] )
# True

any( [0,0,0,1] )
# True


any( [1,2,3] )
# True

any( [1,2,3,0] )
# True

any( [1,2,3,0] )

# Both 0 & "" are False.
any( [0,0,0,0] )
# False

any( ["","","",""] )
# False

any( [0,""] )
# False

#%% chr
#   chr(i) is num2ascii.
#   Given an integer between 0 & 127, chr returns an ASCII code 
#     corresponding to the given integer.
#   Refer to:
#     ASCII Table and Description
#     http://www.asciitable.com/
chr(97)
#'a'
chr(48)
#'0'

#%% dir
#   dir은 객체가 자체적으로 가지고 있는 변수와 함수를 보여준다.
#   TODO: 무슨 말인지 잘 이해가 안 감.

# 리스트의 관련 함수
dir( [1,2,3] )
#['__add__',
# '__class__',
# '__contains__',
# '__delattr__',
# '__delitem__',
# '__dir__',
# '__doc__',
# '__eq__',
# '__format__',
# '__ge__',
# '__getattribute__',
# '__getitem__',
# '__gt__',
# '__hash__',
# '__iadd__',
# '__imul__',
# '__init__',
# '__init_subclass__',
# '__iter__',
# '__le__',
# '__len__',
# '__lt__',
# '__mul__',
# '__ne__',
# '__new__',
# '__reduce__',
# '__reduce_ex__',
# '__repr__',
# '__reversed__',
# '__rmul__',
# '__setattr__',
# '__setitem__',
# '__sizeof__',
# '__str__',
# '__subclasshook__',
# 'append',
# 'clear',
# 'copy',
# 'count',
# 'extend',
# 'index',
# 'insert',
# 'pop',
# 'remove',
# 'reverse',
# 'sort']

# 딕셔너리의 관련 함수
dir( {'1':'a'})
#['__class__',
# '__contains__',
# '__delattr__',
# '__delitem__',
# '__dir__',
# '__doc__',
# '__eq__',
# '__format__',
# '__ge__',
# '__getattribute__',
# '__getitem__',
# '__gt__',
# '__hash__',
# '__init__',
# '__init_subclass__',
# '__iter__',
# '__le__',
# '__len__',
# '__lt__',
# '__ne__',
# '__new__',
# '__reduce__',
# '__reduce_ex__',
# '__repr__',
# '__setattr__',
# '__setitem__',
# '__sizeof__',
# '__str__',
# '__subclasshook__',
# 'clear',
# 'copy',
# 'fromkeys',
# 'get',
# 'items',
# 'keys',
# 'pop',
# 'popitem',
# 'setdefault',
# 'update',
# 'values']

#%% divmod
#   [a%b, a//b] = divmod(a,b)
#   divmod는 a를 b로 나눈 몫 (a%b)과 나머지 (a//b)를 Tuple형태로 리턴한다.
divmod( 7, 3 )
# (2, 1)

divmod( 1.3, 0.2 )  # GREP:
# GREP: (6.0, 0.09999999999999998)
# GREP: The answer should be (6.0, 0.1).
# GREP: I don't like it

#%% enumerate
# enumerate 열거하다...는 순서가 있는 자료형 (리스트, 튜플, 문자열), 즉 sequence container,
# 을 입력 받아 인덱스 값을 포함하는 enumerate객체를 리턴한다.
#
# (객체가 현재 어느 위치에 있는지 알려주는)
# index값이 필요할 때, for와 enumerate를 함께 쓰면 된다.

for i, name in enumerate(['body', 'foo', 'bar']):
    print( i, name )
#0 body
#1 foo
#2 bar

#%% eval
#  eval( expression )은 실행 가능한 문자열 (예: 1+2)을 입력받아 실행한다.
# 보통 입력받은 문자열로 파이썬 함수, 클래스를 동적으로 실행하고 싶을 때 사용한다.    
print( eval('1+2') )
# 3
print( eval(" 'hello'+',world' ") )
# hello,world
print( eval( 'divmod(4,3)' ) )
# (1,1)

#%% filter
#  첫 번째 인수 = 함수이름
#  두 번째 인수 = 함수에 차례로 들어갈 반복가능한 자료형
#  
#  두 번째 인수 (반복 가능한 자료형 요소)들이 (첫 번째 인수인) 함수에 들어갔을 때,
#  리턴값이 참인 것만 묶어서 리턴한다.

#%% positive.py
def positive( numberList ):
    result = []
    for num in numberList:
        if num > 0:
            result.append( num )
    return result

print( positive([1,-3,2,0,-5,6]) )
# [1, 2, 6]

#%% filter.py
#  filter함수를 쓰면 위의 함수를 간단히 구현할 수 있다.

def positive2(x):
    return x>0

print( list( filter( positive2, [1,-3,2,0,-5,6] )) )
# [1, 2, 6]

# 위의 라인을 조금 풀어서 쓰면 다음과 같다.
result = filter( positive2, [1,-3,2,0,-5,6] )
print( list( result) )
# [1, 2, 6]

print( result )
# <filter object at 0x00000173D75FEC50>
print( type( result) )
# <class 'filter'>

#%% lambda함수를 이용하면 더욱 간편히 코드를 작성할 수 있다.
print( list( filter( lambda x:x>0, [1,-3,2,0,-5,6] ) ) )
# [1, 2, 6]

#%% hex
#  정수값을 16진수로 변환해준다.
print( hex(234) )
#0xea
print( hex(3) )
#0x3

#%% id
#  id( object )는 객체를 입력받아 객체의 ID 고유주소값(레퍼런스)를 리턴한다.
a = 3
print( id(3) )
# 140714224751488
print( id(a) )
# 140714224751488
b = a
print( id(b) )
# 140714224751488
# 3,a,b는 ID가 모두 동일하으로 모두 같은 객체를 가리키고 있음을 알 수 있다.

print( id(4) )
# 140714224751520
# 4는 다른 객체이므로 ID가 달라진다.

#%% input
#  input( [prompt] )는 사용자 입력을 받는다.

# 사용자가 입력한 정보를 변수a에 저장
a = input()
print( a )  # hi라고 입력
# 'hi'

# Enter: 라는 프롬프트를 띄우고 사용자 입력을 받는다.
b = input('Enter:')  # hi라고 입력
print( b )
# 'hi'

#%% int
#  int(x)는 문자열 형태의 숫자, 소수점을 정수형태로 리턴한다.
print( int('3') )
# 3
print( int(3.4) )
# 3

# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 리턴한다.
# radix=2, 즉 2진수로 표현된 11을 10진수로 표현한다.
print( int('11',2) )
# 3

# radiox=16, 16진수인 1A를 10진수로 변
print( int('1A',16) )
# 26

print( int('1a',16) )
# 26

# radix=15로 변경해도 동작한다!
print( int('1a',15) )
# 25

#%% isinstance 
#  isinstance( object,class)는
#    첫 번째 인수로 인스턴스
#    두 번째 인수로 클래스 이름을 받는다.
#    해당 인스턴스가, 그 클래스의 인스턴스이면 참, 아니면 거짓을 리턴.

class Person: pass  # 아무 기능이 없는 Person Class를 생성

a = Person()
print( isinstance(a, Person) )
# True

b = 3
print( isinstance(b, Person) )
# False

#%% lambda (예약어)
#  lambda함수를 생성. def와 동일한 역할을 한다.
# - 함수를 한 줄로 간결하게 만들 때 사용함.
#  def를 사용하지 않는 간단한 함수, 혹은 def를 사용할 수 없을 때 주로 쓰인다.
#  사용법
#    lambda 인수1, 인수2, ..., 인수n : 인수를 이용한 표현식

# def sum(a,b):
#   return a+b
#이 함수와 아래 lambda함수는 동일하다.

sum = lambda a,b:a+b
print( sum(3,4) )
# 7

# def를 사용할 수 없는데, lambda는 가능한 경우

myList = [ lambda a,b:a+b, lambda a,b:a*b]
print( myList )
# [<function <lambda> at 0x00000173D767C620>, <function <lambda> at 0x00000173D767C598>]

myList[0]
#<function __main__.<lambda>(a, b)>
myList[0](3,4)
# 7

myList[1]
#<function __main__.<lambda>(a, b)>
myList[1](3,4)
# 12

#%% len
#   len(s)은 입력값의 길이 (요소의 전체 개수)를 리턴한다.

len('Python')
# 6
len([1,2,3])
# 3
len([1,'a'])
# 2

len( [[1,2,3],[4,5,6]] )
# 2

len( [[1,2,3],[4,5,6],[7,8,9]] )
# 3

#%% list
#   list(s)는 반복 가능한 자료형 s를 입력받아 리스트를 리턴한다.
#
# 5 Basic iterable data types
#   Strings
#   Tuples
#   Lists
#   Sets
#   Dictionaries

# string -> list
list('Python')
# ['P', 'y', 't', 'h', 'o', 'n']

# tuple -> list
list( (1,2,3) )
# [1, 2, 3]

a = [1,2,3]
b = list(a)
b
# [1, 2, 3]

#%% map
#   map(f, iterable)은 함수 f와 반복가능한 자료형 (iterable)을 입력으로 받아서,
#   자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴한다.
#
# 5 Basic iterable data types
#   Strings
#   Tuples
#   Lists
#   Sets
#   Dictionaries

#%% two_times.py
#  각 요소에 2를 곱한다.
def two_times( numberList ):
    result = []
    for number in numberList:
        result.append( number*2 )
    return result

result = two_times( [1,2,3,4] )
print( result )
# [2, 4, 6, 8]

#%% map-two_times.py
#  map함수로 위의 함수를 아래처럼 변환할 수 있다.

def two_times(x): return x*2
list( map( two_times, [1,2,3,4] ) )
# [2, 4, 6, 8]

#%% map_and_lambda-two_times.py
list( map( lambda x:x*2, [1,2,3,4]) )
# [2, 4, 6, 8]

# 새로운 함수
#%% map_test.py
def plus_one(x):
    return x+1

list( map(plus_one, [1,2,3,4,5]) )
# [2, 3, 4, 5, 6]

# def 대신 lambda로 구현한 버
#%% map_lambda_test.py

list( map( lambda x:x+1,[1,2,3,4,5]) )
# [2, 3, 4, 5, 6]

#%% max
#   max( iterable )은 반복가능한 자료형의 최대값을 리턴한다.
max( [1,2,3] )
# 3
max( 'python' )
# 'y'

#%% min
#   min( iterable )은 반복가능한 자료현의 최소값을 리턴한다.
min( [1,2,3] )
# 1
min( 'python' )
# 'h'

#%% oct
#   oct(x)는 정수를 입력받아 8진수 문자열로 리턴한다.

oct(34)
# '0o42'
oct(12345)
# '0o30071'

#%% open
#   open( filename, [mode] )는 '파일명'과 '열기방법'을 입력받아서 파일객체를 리턴한다.
#
# mode 설명
# r    read    파일을 읽
# w    write   파일에 쓰기
# a    append  파일에 추가 (append)
# b    binary  바이너리 모드로 파일열기
#   **b는 r,w,a와 함께 사용된다.**

# 2개는 동일하
f_read  = open('read_mode.txt','r')
f_read2 = open('read_mode.txt')

f_append = open('append_mode.txt','a')

# **b는 r,w,a와 함께 사용된다.**
f = open('binary_file','rb')

#%% ord
#   ord(c)는 문자의 아스키코드값을 리턴한다.
ord('a')
# 97

ord('o')
# 111

#%% pow
#   pow(x,y)는 x^y
pow(2,4)
# 16

pow(3,3)
# 27

#%% range
#   range( [start,] stop [,step] )는 입력받은 숫자의 값을
#   반복가능한 객체로 만들어 리턴한다. for문과 함께 자주 사용된다.

# 인수 1개
range(5)
# range(0, 5)
list( range(5) )
# [0, 1, 2, 3, 4]

# 인수 2개
range(5,10)
# range(5, 10)
list(range(5,10))
# [5, 6, 7, 8, 9]

# 인수 3개
range(1, 10, 2)
# range(1, 10, 2)
list( range(1, 10, 2) )
# [1, 3, 5, 7, 9]

#%% sorted
#   sorted( iterable )은 입력값을 정렬 후 리스트로 리턴한다.

# list of integers
sorted( [3,1,2] )
# [1, 2, 3]

# list of characters
sorted( ['a','c','b'] )
# ['a', 'b', 'c']

# string
sorted('zero')
# ['e', 'o', 'r', 'z']

sorted( (3,2,1) )
# [1, 2, 3]

#%% list의 sort
# 리스트 자료형에 sort함수가 있다. 이것은 정렬만하고 정렬된 결과를 리턴하지 않는다.

a = [3,1,2]
result = a.sort()
print( result )
# None
# 리턴값이 없으므로 None이 출력된다.
print(a)
# [1, 2, 3]

#%% str
#   str( object )는 문자열 형태로 객체를 변환해서 리턴한다.
str(3)
# '3'

str('hi')
# 'hi'

str('hi'.upper() )
# 'HI'

#%% tuple
#   tuple( iterable )은 반복가능한 자료형을 입력받아 튜플형태로 바꿔소 리턴한다.
tuple('abc')
# ('a', 'b', 'c')
tuple([1,2,3])
# (1, 2, 3)
tuple( (1,2,3) )
# (1, 2, 3)

#%% type
#   type( object)는 입력값의 자료형이 무엇인지 알려준다.

type('abc')
# str

type( [] )
# list

type( open('test','w') )
# _io.TextIOWrapper

#%% zip
#   zip( iteragble* )은 동일한 개수로 이루어진 자료형을 묶어주는 역할을 한다.

list( zip( [1,2,3],[4,5,6] ) )
# [(1, 4), (2, 5), (3, 6)]

list( zip( [1,2,3],[4,5,6],[7,8,9] ) )
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

list( zip('abc','def') )
# [('a', 'd'), ('b', 'e'), ('c', 'f')]
