# -*- coding: utf-8 -*-
"""
j2p-02_4-tuple.py

P.79, 튜플 자료형

"""

#%%#####################
# 튜플은 어떻게 만들까? #
########################
# 튜플은 몇 가지 점을 제외하곤 리스트와 거의 비슷하다.
# 다른 점은
            # 1. 튜플은 (,)로 둘러싼다. 리스트는 [,]
            # 2. 튜플은 생성된 값을 바꿀 수 없다. 리스트는 가능하다.
            #      A tuple is immutable while a list is mutable.

t1 = ()
t2 = (1,)   # 3. 1개의 요소만 가질 때는 콤마 ,를 반드시 붙여줘야 한다. # GREP
t3 = (1,2,3)
t4 = 1,2,3  # 4. ()를 생략해도 무방하다.
t5 = ('a','b',('ab','cd') )

#%%###################################################
# 튜플의 요소값을 지우거나 변경하려고 하면 어떻게 될까? #
######################################################
# 1. 튜플 요소값 삭제 시 오류

# t1 = (1,2,'a','b')
# del t1[0]
# TypeError: 'tuple' object doesn't support item deletion

# 2. 튜플 요소값 변경 시 오류
# t1 = (1,2,'a','b')
# t1[0] = 'c'
# TypeError: 'tuple' object does not support item assignment

#%%#######################################
# 튜플의 인덱싱과 슬라이싱, 더하기와 곱하기 #
##########################################
# 1. 인덱싱 하기
t1 = (1,2,'a','b')
print( t1[0] )
# 1
print( t1[3] )
# b

# 2. 슬라이싱 하기
t1 = (1,2,'a','b')
print( t1[1:] )
# (2, 'a', 'b')

# 3. 튜플 더하기
t2 = ( 3,4 )
print( t1 + t2 )
# (1, 2, 'a', 'b', 3, 4)

# 4. 튜플 더하기
print( t2*3 )
# (3, 4, 3, 4, 3, 4)