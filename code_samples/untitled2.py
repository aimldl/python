#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:32:22 2020

@author: aimldl
"""

test_string = "A series of string this is a test can be repeated many times like this is a test and this is a test. this is a test "

import re

output = re.findall('this is a test', test_string )
print( output )

p = re.compile('this is a test')
print( len( p.findall( test_string ) ) )