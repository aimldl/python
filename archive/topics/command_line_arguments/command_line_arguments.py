#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
command_line_arguments.py
  Draft: 2019-11-13 (Wed)

This is a class version of test-getopt_full.py at  
  https://github.com/aimldl/python3/blob/master/topics/command_line_arguments/test-getopt_full.py

Example:
  $ python command_line_arguments.py -c conf.txt -i in.txt -o out.txt
  argc=7
  argv=['-c', 'conf.txt', '-i', 'in.txt', '-o', 'out.txt']
  sys.argv[0]=/home/aimldl/command_line_arguments.py
  sys.argv[1]=-c
  sys.argv[2]=conf.txt
  sys.argv[3]=-i
  sys.argv[4]=in.txt
  sys.argv[5]=-o
  sys.argv[6]=out.txt
  opts=[('-c', 'conf.txt'), ('-i', 'in.txt'), ('-o', 'out.txt')]
  args=[]
  config_file=conf.txt
  input_file=in.txt
  output_file=out.txt
  $
"""
import sys, getopt

class CommandLineArguments:
    # This class is assumed to be a singleton.

    # Constructor
    def __init__(self):
        pass

    # Member functions
    def print_inputs( self, argc, argv ):
        print(f"argc={argc}" )
        print(f"argv={argv}" )
        for index in range(argc):
            sys_argv = sys.argv[ index ]
            print(f"sys.argv[{index}]={sys_argv}" )
    
    def main( self, argc, argv, debug=False ):
        if debug:
            self.print_inputs( argc, argv )
        
        # When "$ python test-getopt_more.py" is run, bypass parse_arguments.
        # Otherwise TypeError occurs in "opts, args = getopt.getopt( argv, ... )".
        #   TypeError: 'NoneType' object is not iterable
        if argc > 1:
            #parse_arguments( argc, argv )
            self.parse_arguments( argc, argv, debug=True )
    
    def parse_arguments( self, argc, argv, debug=False ):
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
            short_options = "hc:i:o:"                                 # Note : is used.
            long_options  = ["help", "config=", "input=", "output="]  # Note = is used.
            # YOU MAY CHANGE THIS PART
    
            opts,args = getopt.getopt( argv, short_options, long_options )
            if debug:
                print(f"opts={opts}" )
                print(f"args={args}" )
        
        except getopt.GetoptError:
            self.usage()
            sys.exit(2)
    
        # YOU MAY CHANGE THIS PART
        config_file = ''
        input_file  = ''
        output_file = ''
        # YOU MAY CHANGE THIS PART
        
        for opt, arg in opts:
            if opt in ("-h", "--help"):
              self.usage()
              sys.exit()
              
            # YOU MAY CHANGE THIS PART
            elif opt in ("-c", "--config"):
              config_file = arg
              if debug:
                  print(f"config_file={config_file}" )
            elif opt in ("-i", "--input"):
              input_file = arg
              if debug:
                  print(f"input_file={input_file}" )
            elif opt in ("-o","--output"):
              output_file = arg
              if debug:
                  print(f"output_file={output_file}" )
            # YOU MAY CHANGE THIS PART
    
            else :
              self.usage()
              sys.exit(2)
    
    def usage( self ):
      print("usage: $ python command_line_arguments.py -h")

if __name__ == "__main__":
    
    cla = CommandLineArguments()
    # Process the command line arguments
    argc = len( sys.argv )
    argv = sys.argv[1:]
    #cla.main( argc, argv )
    cla.main( argc, argv, debug=True )

# EOF    
