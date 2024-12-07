#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
aimldl > python3 > topics > command_line_arguments > tutorialspoint.com > test-simple_example.py
  Rev.2: 2019-11-07 (Thu)
  Rev.1: 2019-03-01 (Fri)
  Draft: 2018-11-08 (Thu)

Source:
  Python - Command Line Arguments
  https://www.tutorialspoint.com/python/python_command_line_arguments.htm

Syntax:
  $ python test-simple_example.py arg1 arg2 arg3
  Number of arguments: 4 arguments.
  Argument List: ['test-simple_example.py', 'arg1', 'arg2', 'arg3']
  $
'''
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

# (EOF)
