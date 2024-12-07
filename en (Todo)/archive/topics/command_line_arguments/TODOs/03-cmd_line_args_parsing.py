# -*- coding: utf-8 -*-
import sys, getopt

# 2019-03-01 (Fri)
#
# TODO1: The following command fails to work. Fix it.
#  $ python3 03-cmd_line_args_parsing.py -h
#  $ python3 03-cmd_line_args_parsing.py --help
# TODO2: Once TODO1 works. Work with more complex examples

def usage():
  print("usage: python3 03-cmd_line_args_parsing.py arg1 arg2 arg3")
  
def print_opts():
  print("file_name =", file_name )
  print("argc      =", argc )
  print("argv      =", argv )
  print("input_file=", input_file )
  print("output_file=", output_file )

def main( argc, argv ):
  print("argv      =", argv )
  print("argc      =", argc )

  try:
    # opts, args = getopt.getopt( argv, "", [])
    #   Input
    #     argv is the (entire) argument list
    #     "" is a short option starting with a hyphen -. Example: -h
    #           An argument should be followed by a colon (:).
    #     [] is a long option start with two hyphens --. Example: --help
    #           An argument should be followed by an equal sign ('=').
    #   Output
    #     opts is a list of (option, value) pairs.
    #     args is the list of program arguments left after the option list was stripped.

    short_opt = "h"
    long_opt  = ["help"]
    opts, args = getopt.getopt( argv, short_opt,long_opt)
    
    print("opts      =", opts )
    print("args      =", args )

  except getopt.GetoptError:
    usage()
    sys.exit(2)  

  for opt, val in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    else :
      usage()
      sys.exit(2)

if __name__ == "__main__":
  # Process the command line arguments
  argc      = len( sys.argv )
  file_name = sys.argv[0]
  argv      = str( sys.argv[1:] )

  print("file_name =", file_name )
  print("sys.argv  =", sys.argv )

  main( argc, argv )

# Last Modified: 2019-03-01 (Fri)
# First Written: 2018-11-08 (Thu)
#
# Tae-Hyung "T" Kim, aimldl@naver.com
#
# There are a couple of popular packages to parse the command line arguments
# such as getopt, argparse, and docopt. My choice is getopt. Note optparse is obsolete.
#
# Ref: Python - Command Line Arguments
#      https://www.tutorialspoint.com/python/python_command_line_arguments.htm
#
# getopt — C-style parser for command line options
# Ref: https://docs.python.org/3/library/getopt.html#module-getopt
#
#  getopt.getopt(argv, options, [long_options])
#
#   argv         is the argument list
#   options      is a short option starting with a hyphen -. Example: -h
#                An argument should be followed by a colon (:).
#   long_options is a long option start with two hyphens --. Example: --help
#                An argument should be followed by an equal sign ('=').
#
# Examples
#   https://www.programcreek.com/python/example/121/getopt.getopt

# This method returns value consisting of two elements: 
#  the first is a list of (option, value) pairs.
#  The second is the list of program arguments left after the option list was stripped.

# Command Examples
#
# $ python3 03-cmd_line_args_parsing.py arg1 arg2 arg3
# 
# $ python 03-cmd_line_args_parsing.py arg1 arg2 arg3
