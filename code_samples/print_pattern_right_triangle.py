#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

def right_triangle( height ):

    stack = []
    
    number_of_spaces=0
    for ii in range( height, 0, -1):
        #if number_of_spaces != 0:
        #    temp_string = " " * number_of_spaces
        temp_string = " " * number_of_spaces
        temp_string += "*"*ii 
        stack.append( temp_string )
        number_of_spaces += 1
    
    for ii in range( height, 0, -1):
        print( stack.pop() )
        
        

#right_triangle( 3 )
#   *
#  **
# ***

#right_triangle( 5 )
#     *
#    **
#   ***
#  ****
# *****