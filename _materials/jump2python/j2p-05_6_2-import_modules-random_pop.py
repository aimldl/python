# -*- coding: utf-8 -*-
'''
j2p-05_6-import_modules-random_pop.py
'''
# random_pop.py
import random
def random_pop( data ):
    number = random.randint( 0, len(data)-1 )
    return data.pop( number )

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data: print( random_pop(data) )

#5
#4
#2
#1
#3