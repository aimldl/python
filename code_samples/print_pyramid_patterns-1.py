#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programs for printing pyramid patterns in Python
  https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/
"""

def pyramid( height ):
    number_of_spaces = 2*height -2
    
    for ii in range( 0, height ):
        for jj in range( 0, number_of_spaces):
            print( end=" " )
        number_of_spaces -= 1

        for jj in range(0, ii):
            print("* ", end="")
        
        print("\r")

# pyramid( 5 )
#       * 
#      * * 
#     * * * 
#    * * * * 

# pyramid( 6 )
#         * 
#        * * 
#       * * * 
#      * * * * 
#     * * * * * 

