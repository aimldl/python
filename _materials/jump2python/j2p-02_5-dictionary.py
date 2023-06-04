# -*- coding: utf-8 -*-
"""
j2p-02_5-dictionary.py

P.82, 딕셔너리 자료형

딕셔너리는 Key-value을 한 쌍으로 갖는 자료형이다.
"""

#%%########################
# 딕셔너리는 어떻게 만들까? #
###########################
dic = {'name':'pey', 'phone':'0119993323','birth':'1118'}

# key=1, value=hi, string type value
a = {1:'hi'}

# key=a, value=[1,2,3], list type value
a = {'a':[1,2,3]}

#%%#########################
# 딕셔너리 쌍 추가/삭제 하기 #
############################
# 1. 딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b'  # {2:'b'} 쌍 추가
print(a)
# {1: 'a', 2: 'b'}

a['name'] = 'pey'
print( a )
# {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1,2,3] 
print( a )
# {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 2. 딕셔너리 요소 삭제하기
del a[1]
print( a )
#{2: 'b', 'name': 'pey', 3: [1, 2, 3]}

#%%#######################
# 딕셔너리를 사용하는 방법 #
##########################
# 딕셔너리에서 Key를 사용해서 Value얻기
grade = {'pey':10 , 'julliet':99 }
print( grade['pey'] )
# 10
print( grade['julliet'] )
# 99

a= {1:'a', 2:'b'}
print( a[1] )
# a
print( a[2] )
# b

a = {'a':1 , 'b':2 }
print( a['a'] )
# 1
print( a['b'] )
# 2

dic = {'name':'pey', 'phone':'0119993323','birth':'1118'}
print( dic['name'] )
# pey
print( dic['phone'] )
# 0119993323

print( dic['birth'] )
# 1118

#%%###########################
# 딕셔너리 만들 때 주의할 사항 #
##############################
#%% 1. Key가 중복되면 안 된다.
a ={1:'a',1:'b'}
print( a )
# {1: 'b'}
# 이렇게 key가 중복되었을 떄 1개를 제외한 나머지 key:value값이 모두 무시된다.
#

#%% 2. Key에 List를 쓸 수 없다.
# a = {[1,2]:'hi'}
# TypeError: unhashable type: 'list

#%% 하지만 Tuple은 Key로 쓸 수 있으므로 혼돈하지 말아야 할 것이다.

#%%####################
# 딕셔너리 관련 함수들 #
#######################

#%%#######################
# Key리스트 만들기 (keys) # 
##########################
a = {'name':'pey', 'phone':'0119993323','birth':'1118'}
print( a.keys() )
# dict_keys(['name', 'phone', 'birth'])

# dict_keys, dict_values, dict_items는
#   반복성 구문 (예: for문)에 리스트로 변환하지 않더라도
#   실행할 수 있다.

for k in a.keys():
  print(k)
#name
#phone
#birth

# 파이썬 3.0이후 버전의 keys함수 어떻게 달라졌나?
#   파이썬 2.7까지는 list를 리턴한다. 그러기 위해서는 메모리의 낭비가 발생한다.
#   그러므로 낭비를 줄이기 위해 파이썬 3.0 이후에는 dict_keys라는 객체를 리턴한다.

# 만약 리스트가 필요한 경우에는
#   list( a.keys() )
# 를 사용하면 된다.
print( list( a.keys() ) )
#['name', 'phone', 'birth']

#%%############################
# Value 리스트 만들기 (values) #
###############################
print( a.values() )
# dict_values(['pey', '0119993323', '1118'])

print( list( a.values()) )
# ['pey', '0119993323', '1118']

#%%###########################
# Key, Value 쌍 얻기 (items) #
##############################

print( a.items() )
# dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

print( list( a.items() ) )
# [('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')]

#%%#################################
# Key: Value 쌍 모두 지우기 (clear) #
####################################
print( a )
#{'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

print( a.clear() )
# None

print( a )
# {}

#%%#######################
# Key로 Value 얻기 (get) #
##########################
a = {'name':'pey', 'phone':'0119993323','birth':'1118'}
print( a.get('name') )
# pey

print( a.get('phone') )
# 0119993323

# 존재하지 않는 키로 값을 가져오려고 할 경우의 차이
#  둘 중에 어느 쪽은 쓰는지는 사용자의 선택임.

# get은 None을 리턴한다.
print( a.get('nokey') )
# None

# a[]는 KeyError를 리턴한다.
print( a['nokey'] )
# KeyError: 'nokey'

# 딕셔너리 안에 찾으려는 key값이 없을 경우,
#   미리 정해둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 
#   get(x,'디폴트값')을 사용하면 편리하다.
# 예: 디폴트값은 'bar'로 설정된 상태.
#     없는 key값인 'foo'를 입력할 경우

print( a.get('foo','bar') )

#%%############################################
# 해당 Key가 딕셔너리 안에 있는지 조사하기 (in) #
###############################################
a = {'name':'pey', 'phone':'0119993323','birth':'1118'}

print( 'name' in a )
# True

print( 'email' in a )
# False