#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programs for printing pyramid patterns in Python
  https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/
"""

def pyramid( height ):

    stack = []
    number_of_spaces = 0
    for h in range( height, 0, -1 ):
        #print( h )
        
        for space in range( 0, number_of_spaces ):
            stack.append( " " )

        number_of_asterisks = 2*h-1            
        for i in range( 0, number_of_asterisks ):
          stack.append( '*' )

        for space in range( 0, number_of_spaces ):
            stack.append( " " )
          
        number_of_spaces +=1

    width = 2*height-1
    for h in range( 1, height+1 ):

        for jj in range(0, width):
            print( stack.pop(), end='' )
        print('')

# pyramid( 4 )
#    *   
#   ***  
#  ***** 
# *******

# pyramid( 7 )
#       *      
#      ***     
#     *****    
#    *******   
#   *********  
#  *********** 
# *************

pyramid( 100 )