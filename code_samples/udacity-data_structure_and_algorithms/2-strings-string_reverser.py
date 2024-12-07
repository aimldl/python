# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    
    # TODO: Write your solution here
    #print( our_string )
    #print( len( our_string) )
    L = len( our_string )
    reversed_string=[]
    new_string=""
    for i in range( L ):
        #print( our_string[L-i-1] )
        reversed_string.append( our_string[L-i-1] )
        new_string += our_string[L-i-1]
    #print( ''.join( reversed_string ) )
    #return ''.join( reversed_string)
    return new_string


if __name__ == '__main__':
    print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
    print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
    print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")