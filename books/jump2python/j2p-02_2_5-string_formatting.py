# -*- coding: utf-8 -*-
"""
j2p-02_2_5-string_formatting.py

P.54, 문자열 포매팅
#%% '#%%' sign separates a file with different hilights in Spyder. # GREP
"""

#%%######################
# 문자열 포매팅 따라하기 #
#########################

# 1. 숫자 바로 대입
print("I eat %d apples" % 3 )
# I eat 3 apples

# 2. 문자열 바로 대입
print("I eat %s apples" % 'five' )
# I eat five apples

# 3. 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples" % number )
# I eat 3 apples

# 5. 2개 이상의 값 넣기
number = 10
day = 'three'

print("I ate %d apples. So I was sick for %s days" % (number, day) )
# I ate 10 apples. So I was sick for three days

#%%################
# 문자열 포맷 코드 #
###################
# 재미있는 것은 %s인데, 어떤 형태의 값을 입력해도 변환해서 출력이 된다.
print('I have %s apples' % 3)
# I have 3 apples

print('rate is %s' % 3.234)
# rate is 3.234

# %s은 정수인 3과 부동소수인 3.234를 문자열로 자동변환했다.

# Code   Description       설명
# %s     string           문자열
# %c     character        문자 1개
# %d     integer/decimal  정수
# %f     floating point   부동 소수
# %o     octal            8진수
# %x     hexa             16진수
# %%     (Literal) %      % 문자

###############################################
# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다. #
################################################
# "Error is 98%"를 출력하려고 할 때, 다음 문법은 ValueError를 낸다.
# print('Error is %d%.' %98)
# ValueError: incomplete format
#
# 에러를 수정하기 위해서는 %%를 써야한다. /%가 아님에 유의 # GREP
print('Error is %d%%.' %98)  # GREP
#Error is 98%.

#%%#############################
# 포맷 코드와 숫자 함께 사용하기 #
################################

# 1.정렬과 공백
print('%10s' %'hi')  # 오른쪽 정렬
# '        hi'

print('%-10s' %'hi')  # 왼쪽 정렬
# 'hi        '

print('%-10sjane' %'hi')  # 왼쪽 정렬
# 'hi        jane'

# 2.소수점 표현하기
print('%0.4f' % 3.42134234 )
# 3.4213

print('%10.4f' % 3.42134234 )
# '    3.4213'
# 전체길이가 10이고, 그 중 소수점은 4자리까지 보여준다.