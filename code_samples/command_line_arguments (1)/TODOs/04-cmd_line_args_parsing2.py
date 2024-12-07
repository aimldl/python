# -*- coding: utf-8 -*-
import sys, getopt

def usage():
  print("usage: python3 04-cmd_line_args_parsing2.py arg1 arg2 arg3")

def print_opts():
  print("file_name =", file_name )
  print("argc      =", argc )
  print("argv      =", argv )
  print("opts      =", opts )
  print("args      =", args )
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

    short_opt = "hi:o:"
    long_opt  = ["help","input=", "output="]
    opts, args = getopt.getopt( argv, short_opt,long_opt)

    print("opts      =", opts )
    print("args      =", args )

  except getopt.GetoptError:
    usage()
    sys.exit(2)

  input_file  = ''
  output_file = ''

  for opt, val in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    elif opt in ("-i", "--input"):
      input_file = arg
    elif opt in ("-o","--output"):
      output_file = arg
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
