#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
aimldl > python3 > topics > command_line_arguments > test-getopt_simple.py
  Rev.3: 2019-11-13 (Wed)
  Rev.2: 2019-11-07 (Thu)
  Rev.1: 2019-03-01 (Fri)
  Draft: 2018-11-08 (Thu)

Examples:
1. No option
    $ python test-getopt_simple.py
    argc=1
    argv=['test-getopt_simple.py']
    file_name=test-getopt_simple.py
    sys.argv[0]=test-getopt_simple.py
    opts=[]
    args=['test-getopt_simple.py']
    $

2. Short option -h
    $ python test-getopt_simple.py -h
    argc=2
    argv=['test-getopt_simple.py', '-h']
    file_name=test-getopt_simple.py
    sys.argv[0]=test-getopt_simple.py
    sys.argv[1]=-h
    opts=[]
    args=['test-getopt_simple.py', '-h']

3. Long option --help
    $ python test-getopt_simple.py --help
    argc=2
    argv=['test-getopt_simple.py', '--help']
    file_name=test-getopt_simple.py
    sys.argv[0]=test-getopt_simple.py
    sys.argv[1]=--help
    opts=[]
    args=['test-getopt_simple.py', '--help']
4. Options not specified in the for loop
    $ python test-getopt_simple.py -i in.txt -o out.txt
    argc=5
    argv=['/home/aimldl/test-getopt_simple.py', '-i', 'in.txt', '-o', 'out.txt']
    sys.argv[0]=/home/aimldl/test-getopt_simple.py
    sys.argv[1]=-i
    sys.argv[2]=in.txt
    sys.argv[3]=-o
    sys.argv[4]=out.txt
    opts=[]
    args=['/home/aimldl/test-getopt_simple.py', '-i', 'in.txt', '-o', 'out.txt']
'''

import sys, getopt

def print_inputs( argc ):
    print(f"argc={argc}" )
    print(f"argv={argv}" )
    for index in range(argc):
        sys_argv = sys.argv[ index ]
        print(f"sys.argv[{index}]={sys_argv}" )
        
def main( argc, argv, debug=False ):
  if debug:
      print_inputs(argc)

  # When "$ python test-getopt_more.py" is run, bypass parse_arguments.
  # Otherwise TypeError occurs in "opts, args = getopt.getopt( argv, ... )".
  #   TypeError: 'NoneType' object is not iterable
  if argc > 1:
      #parse_arguments( argc, argv )
      parse_arguments( argc, argv, debug=True )

def parse_arguments( argc, argv, debug=False ):
    '''
    opts,args = getopt.getopt( argv,"",[] )
    Input
      argv is the (entire) argument list
         "" is a short option starting with a hyphen -. Example: -h
               An argument should be followed by a colon (:).
         [] is a long option start with two hyphens --. Example: --help
               An argument should be followed by an equal sign ('=').
    Output
      opts is a list of (option, value) pairs.
      args is the list of program arguments left after the option list was stripped.
    '''
    assert isinstance(argc, int), 'argc must be an integer'
    assert isinstance(argv, list), 'argv must be a list'

    try:
        # YOU MAY CHANGE THIS PART
        short_options = "h"       # Note : is used.
        long_options  = "help"  # Note = is used.
        # YOU MAY CHANGE THIS PART

        opts, args    = getopt.getopt( argv, short_options, long_options)
        if debug:
            print(f"opts={opts}" )
            print(f"args={args}" )

    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
          usage()
          sys.exit()
        else :
          usage()
          sys.exit(2)

def usage():
  print("usage: $ python test-getopt_simple.py -h")

if __name__ == "__main__":
  # Process the command line arguments
  argc      = len( sys.argv )
  argv      = sys.argv[1:]
  #main( argc, argv )
  main( argc, argv, debug=True )

# EOF
