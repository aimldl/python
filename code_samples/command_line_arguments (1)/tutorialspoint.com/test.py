#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
aimldl > python3 > topics > command_line_arguments > tutorialspoint.com > test.py
  Rev.2: 2019-11-07 (Thu)
  Rev.1: 2019-03-01 (Fri)
  Draft: 2018-11-08 (Thu)

Source:
  Python - Command Line Arguments
  https://www.tutorialspoint.com/python/python_command_line_arguments.htm

Syntax:
  $ python test.py -h
  test.py -i <inputfile> -o <outputfile>

  $ python test.py -i english.pcm -o english.wav
  Input file is " english.pcm
  Output file is " english.wav

  $ python test.py -i BMP -o
  test.py -i <inputfile> -o <outputfile>

  $ python test.py -i inputfile
  Input file is " inputfile
  Output file is "
  $
'''

import sys, getopt

def main( argv ):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('Input file is "', inputfile)
   print('Output file is "', outputfile)

if __name__ == "__main__":
   main( sys.argv[1:] )
# (EOF)
