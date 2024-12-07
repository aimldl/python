#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Divisor
  https://byjus.com/maths/divisor/#:~:text=Divisor%20Meaning&text=So%2C%20the%20number%20which%20is,is%20referred%20to%20as%20remainder.

  Dividend ÷ Divisor = Quotient
  Divisor = Dividend ÷ Quotient
  Dividend / Divisor = Quotient

약수, 배수, 공약수, 소수는 영어로 뭘까?, 2019-11-13
  https://m.blog.naver.com/qufgnsid/221706424480

소수: prime number

약수: divisor
공약수: common divisor
최대공약수: Greatest common denominator (GCD)

배수: multiple
공배수: common multiple
최소공배수: Least common multiple (LCM)

"""

def print_divisors( number ):
    assert isinstance( number, int )
    
    for divisor in range( 1, number+1 ):
        quotient = number % divisor
        if quotient == 0:
            print( divisor, end=' ')
    print('')


# main
input_number = int( input( "Enter an integer:") )
print( str(input_number)+':', end=' ' )
print_divisors( input_number )

# Enter an integer:134
# 134: 1 2 67 134 

for integer_number in range(1, 1002):
    print( str(integer_number)+':', end=' ')
    print_divisors( integer_number )

# 1: 1 
# 2: 1 2 
# 3: 1 3 
# 4: 1 2 4 
# 5: 1 5 
# 6: 1 2 3 6 
# 7: 1 7 
# 8: 1 2 4 8 
# 9: 1 3 9 
# 10: 1 2 5 10 
# 11: 1 11 
# 12: 1 2 3 4 6 12 
# 13: 1 13 
# 14: 1 2 7 14 
# 15: 1 3 5 15 
# 16: 1 2 4 8 16 
# 17: 1 17 
# 18: 1 2 3 6 9 18 
# 19: 1 19 
# 20: 1 2 4 5 10 20 