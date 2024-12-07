#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
p4e-8_4_more_string_methods.py
pandas_for_everyone

8. Strings and Text Data
  8.1. Introduction
  8.2. Strings
    8.2.1. Subsetting and Slicing Strings
      8.2.1.1. Single Letter
      8.2.1.2. Slicing Multiple Letters
      8.2.1.3. Negative Numbers
    8.2.2. Getting the Last Character in a String
      8.2.2.1. Slicing from the Beginning or to the End
      8.2.2.1. Slicing Increments
  8.3. String Methods
  8.4. More String Methods
    8.4.1. Join
    8.4.2. Splitlines
    # Removing every other line #
    # Removing every other line & the leading prefix #
"""
"""
# Summary
## join
## splitlines
## Removing every other line
multi_str_splitlines = multi_str.splitlines()[::2]
## Removing every other line & the leading prefix
"""
############################
# 8. Strings and Text Data #
############################

############################
# 8.4. More String Methods #
############################

###############
# 8.4.1. Join #
###############
# Use the DMS (Degrees Minutes Seconds) notation

d1 = '40°'
m1 = "46'"
s1 = '52.837"'
u1 = 'N'

d2 = '73°'
m2 = "58'"
s2 = '26.302"'
u2 = 'W'

coords = ' '.join( [d1, m1, s1, u1, d2, m2, s2, u2] )
print( coords )
#40° 46' 52.837" N 73° 58' 26.302" W


#####################
# 8.4.2. Splitlines #
#####################

multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using conconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together"""
print( multi_str )
#Guard: What? Ridden on a horse?
#King Arthur: Yes!
#Guard: You're using conconuts!
#King Arthur: What?
#Guard: You've got ... coconut[s] and you're bangin' 'em together

# splitlines splits each line as an element of a list
#   and returns the list.
multi_str_splitlines = multi_str.splitlines()
print( multi_str_splitlines )
#['Guard: What? Ridden on a horse?',
# 'King Arthur: Yes!',
# "Guard: You're using conconuts!",
# 'King Arthur: What?',
# "Guard: You've got ... coconut[s] and you're bangin' 'em together"]

#############################
# Removing every other line #
#############################

# Guard speaks every other line.
#   So every other line can be extracted only for Guard.
guard = multi_str_splitlines[::2]
print( guard )
#['Guard: What? Ridden on a horse?',
# "Guard: You're using conconuts!",
# "Guard: You've got ... coconut[s] and you're bangin' 'em together"]

# Well, the above steps are done in a single line!
# Isn't it cool? Yeah!
print( multi_str.splitlines()[::2] )
#['Guard: What? Ridden on a horse?',
# "Guard: You're using conconuts!",
# "Guard: You've got ... coconut[s] and you're bangin' 'em together"]

##################################################
# Removing every other line & the leading prefix #
##################################################
# Since 'Guard:' is repeated, it can be removed 
#   by replacing it to an empty string ''.

# The following lines won't work because of the AttributeError.
#guard_without_prefix = guard.replace('Guard:','')
#print( guard_without_prefix )
#AttributeError: 'list' object has no attribute 'replace'

multi_str_replace_splitlines = multi_str.replace('Guard: ', '').splitlines()[::2]
print( multi_str_replace_splitlines )
#['What? Ridden on a horse?',
# "You're using conconuts!",
# "You've got ... coconut[s] and you're bangin' 'em together"]
#
# I think this one line of code is elegant!