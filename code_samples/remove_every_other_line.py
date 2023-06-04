# -*- coding: utf-8 -*-
'''
remove_every_other_line.py

Written on 2018-11-22 (Thu)

'''

import sys

#filename = sys.argv[1]
filename = 'new_1.py'

print('Removing every other line in', filename)
with open( filename, 'r', encoding='utf-8') as f:
	for line in f:
		print( line )


"""
Errors

Problem
UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 0: illegal multibyte sequence

Error message
Traceback (most recent call last):
  File "remove_every_other_line.py", line 16, in <module>
    for line in f:
UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 0: illegal multibyte sequence

Hint
http://hianna.tistory.com/290

Solution
with open( filename, 'r', encoding='utf-8') as f:

* UnicodeEncodeError: 'cp949' codec can't encode character '\u200b' in position 0: illegal multibyte sequence


"""