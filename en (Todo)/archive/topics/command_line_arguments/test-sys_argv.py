#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
aimldl > python3 > topics > command_line_arguments > test-sys_argv.py
  Rev.3: 2019-11-13 (Wed)
  Rev.2: 2019-11-07 (Thu)
  Rev.1: 2019-03-01 (Fri)
  Draft: 2018-11-08 (Thu)

Syntax:
  $ python test-sys_argv.py arg1 arg2 arg3
  argc=4
  argv=['/home/aimldl/test-sys_argv.py', 'arg1', 'arg2', 'arg3']
  sys.argv[0]=/home/aimldl/test-sys_argv.py
  sys.argv[1]=arg1
  sys.argv[2]=arg2
  sys.argv[3]=arg3
  $
  
  $ python test-sys_argv.py -i in.txt -o out.txt
  argc=5
  argv=['/home/aimldl/test-sys_argv.py', '-i', 'in.txt', '-o', 'out.txt']
  sys.argv[0]=/home/aimldl/test-sys_argv.py
  sys.argv[1]=-i
  sys.argv[2]=in.txt
  sys.argv[3]=-o
  sys.argv[4]=out.txt
  $
'''

import sys

def print_inputs( argc ):
    print(f"argc={argc}" )
    print(f"argv={argv}" )
    for index in range(argc):
        sys_argv = sys.argv[ index ]
        print(f"sys.argv[{index}]={sys_argv}" )

def main( argc, argv, debug=False ):
  if debug:
      print_inputs(argc)

'''
Caution:
  argv should not be a string.
  If argv is a string, getopt.getopt( argv, ... ) won't work as it should be.
    BAD:  argv = str( sys.argv )
    GOOD: argv = sys.argv[1:]
'''     
if __name__ == "__main__":
  # Process the command line arguments
  argc      = len( sys.argv )
  argv      = sys.argv[1:]
  
  #main( argc, argv )
  main( argc, argv, debug=True )

# EOF
