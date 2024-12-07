# -*- coding: utf-8 -*-
"""
pnlp-4_preprocessing-regular_expression.py

Source: Python Natural Language Processing
Advanced machine learning and deep learning techniques for natural language processing
Jalaj Thanaki

파이썬 자연어 처리의 이론과 실제
효율적인 자연어 처리를 위한 머신 러닝과 딥러닝 구현하기
04. 전처리 > 기본 전처리 > 정규 표현식
pp.125~135

regex or regular expression
Basic flag
  re.I  Ignore-case
  re.M  Multi-line
        In the textbook, re.M is given, but actually it's not necessary for the
        given inputs.
"""

import re

#%%#######################
# re.search vs. re.match #
##########################

def search_vs_match():  # p.127
    line = 'I love animals.'

    #############
    # re.search #
    #############
    # is more forgiving.
    #search_obj = re.search(r'animals', line, re.M | re.I)
    search_obj = re.search(r'animals', line, re.I)
    if search_obj:
        print('search_obj:' , search_obj.group() )
    else:
        print('Nothing found!')
#   searchObj: animals
    
    ############
    # re.match #
    ############
    # is very strict.
    #match_obj = re.match(r'animals', line, re.M | re.I)
    match_obj = re.match(r'animals', line, re.I)
    if match_obj:
        print('match_obj:', match_obj.group() )
    else:
        print('No match!')
#   No match!
        
#%%########################
# Examples of basic regex #
###########################
def basic_regex():
    line         = 'This is a test sentence and the test sentence is also a sentence.'
    contact_info = 'Doe, John: 1111-1212'
    phone        = '1111-2222-3333 # This is a phone number.'

    ##############
    # re.findall #
    ##############
    # Find all occurences of sentence from line.    
    findall_obj = re.findall(r'sentence', line)
    print( findall_obj )
#   ['sentence', 'sentence', 'sentence']

    ########################
    # re.search with regex #
    ########################
    # Search 'something, something: ' from contact_info.
    group_wise_obj = re.search(r'(\w+), (\w+): (\S+)', contact_info)  # \S+ is correct, \s+ isn't!
    # r'(\w+), (\w+): (\S+)' means(?) 'word 1 or more, word 1 or more: Not space 1 or more.'
    print('group(1) =', group_wise_obj.group(1) )
    print('group(2) =', group_wise_obj.group(2) )
    print('group(3) =', group_wise_obj.group(3) )
#   group(1) = Doe
#   group(2) = John
#   group(3) = 1111-1212

    ######################
    # re.sub to replaces #
    ######################
    # Replace John to Peter in contact_info
    contact_info_revised = re.sub(r'John', 'Peter', contact_info)
    print('contact_info_revised =', contact_info_revised)
#   contact_info_revised = Doe, Peter: 1111-1212
    
    ####################
    # re.sub to delete #
    ####################
    # Delete the Python-style comment at the end of the sentence
    # That is, delete '# This is a phone number.' from phone.
    num = re.sub(r'#.*$', '', phone)
    # #.*$ means(?) # followed by a character (.) and all (*) from the end ($)
    print('num =', num)
#   num = 1111-2222-3333 # This is a phone number.    
    
    # Note: the following expressions don't work!
    #num = re.sub(r'#*$', '', phone)
    #num = re.sub(r'#\s*$', '', phone)    

#%%################################################
# Advanced regex: Positive vs. Negative Lookahead #
###################################################
def advanced_regex():
    text = 'I play on playground. it is the best ground.'

    ######################
    # Positive Lookahead #
    ######################
    
    #####################
    # r'play(?=ground)' #
    #####################
    #positive_lookahead = re.findall(r'play(?=ground)', text, re.M| re.I)
    positive_lookahead = re.findall(r'play(?=ground)', text, re.I)
    print('positive_lookahead =', positive_lookahead)
#   positive_lookahead = ['play']
    
    positive_lookahead = re.search(r'play(?=ground)', text, re.I)
    print('positive_lookahead character index =', positive_lookahead.span() )
#   positive_lookahead character index = (10, 14)

    ######################
    # r'(?<=play)ground' #
    ######################
    positive_lookahead = re.findall(r'(?<=play)ground', text, re.I)
    print('positive_lookahead =', positive_lookahead)
#   positive_lookahead = ['ground']
    
    positive_lookahead = re.search(r'(?<=play)ground', text, re.I)
    print('positive_lookahead character index =', positive_lookahead.span() )
#   positive_lookahead character index = (14, 20)

    ######################
    # Negative Lookahead #
    ######################
    
    #####################
    # r'play(?!ground)' #
    #####################
    negative_lookahead = re.findall(r'play(?!ground)', text, re.I)
    print('negative_lookahead =', negative_lookahead)
#   negative_lookahead = ['play']
    
    negative_lookahead = re.search(r'play(?!ground)', text, re.I)
    print('negative_lookahead character index =', negative_lookahead.span() )
#   negative_lookahead character index = (2, 6)

    ######################
    # r'(?<=play)ground' #
    ######################
    negative_lookahead = re.findall(r'(?<=play)ground', text, re.I)
    print('negative_lookahead =', negative_lookahead)
#   negative_lookahead = ['ground']
    
    negative_lookahead = re.search(r'(?<=play)ground', text, re.I)
    print('negative_lookahead character index =', negative_lookahead.span() )
#   negative_lookahead character index = (14, 20)
  
    
if __name__ == '__main__':
    print('re.match() vs. re.search()')
#   re.match() vs. re.search()
    
    search_vs_match()
#   re.match() vs. re.search()
#   searchObj: animals
#   No match!
    
    basic_regex()
#   ['sentence', 'sentence', 'sentence']
#   group(1) = Doe
#   group(2) = John
#   group(3) = 1111-1212
#   contact_info_revised = Doe, Peter: 1111-1212
#   num = 1111-2222-3333 

    advanced_regex()
#   positive_lookahead = ['play']
#   positive_lookahead character index = (10, 14)
#   positive_lookahead = ['ground']
#   positive_lookahead character index = (14, 20)
#   negative_lookahead = ['play']
#   negative_lookahead character index = (2, 6)
#   negative_lookahead = ['ground']
#   negative_lookahead character index = (14, 20)
