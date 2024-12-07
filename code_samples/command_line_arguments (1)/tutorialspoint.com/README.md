##### aimldl > python3 > topics > command_line_arguments > tutorialspoint.com > README.md
* Rev.2: 2019-11-13 (Wed)
* Rev.1: 2019-03-01 (Fri)
* Draft: 2018-11-08 (Thu)

# Simple Example Scripts for Command Line Arguments in Python
The following scripts show how to use command line arguments in Python3.
1. [test-simple_example.py](test-simple_example.py)
2. [test.py](test.py)

which are taken from [Python - Command Line Arguments](https://www.tutorialspoint.com/python/python_command_line_arguments.htm).

### Changes
This tutorial is written for Python2. So the Python scripts fail to run in Python3 because of SyntaxErrors which are fixed as follows.
* [test-simple_example.py](test-simple_example.py),
  * Old
    * print 'Number of arguments:', len(sys.argv), 'arguments.'
    * print 'Argument List:', str(sys.argv)
  * New
    * print('Number of arguments:', len(sys.argv), 'arguments.')
    * print('Argument List:', str(sys.argv))
* [test.py](test.py)
  * Old
    * print 'test.py -i <inputfile> -o <outputfile>'
    * print 'test.py -i <inputfile> -o <outputfile>'
    * print 'Input file is "', inputfile
    * print 'Output file is "', outputfile
  * New
    * print('test.py -i <inputfile> -o <outputfile>')
    * print('test.py -i <inputfile> -o <outputfile>')
    * print('Input file is "', inputfile)
    * print('Output file is "', outputfile)

### 1. test-simple_example.py
***Excerpts from [Python - Command Line Arguments](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)***
Python provides a getopt module that helps you parse command-line options and arguments.
```bash
    $ python script_name.py arg1 arg2 arg3
```
Python's sys module provides access to any command-line arguments via sys.argv where sys.argv[0] contains the script name. This serves two purposes:
1. sys.argv is the list of command-line arguments.
2. len(sys.argv) is the number of command-line arguments.

Run this script as follows:
```bash
    $ python test-simple_example.py arg1 arg2 arg3
    Number of arguments: 4 arguments.
    Argument List: ['test-simple_example.py', 'arg1', 'arg2', 'arg3']
    $
```

### 2. test.py
***Excerpts from [Python - Command Line Arguments](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)***
Python provided the getopt module that helps you parse command-line options and arguments. This module provides two functions. The first function ***getopt*** parses the command-line arguments. The second function ***GetoptError*** handles the exception happened during command line argument parsing.

1. ***getopt.getopt method***
```python
    getopt.getopt(args, options, [long_options])
```
returns value consisting of two elements:
1. a list of (option, value) pairs,
2. the list of program arguments left after the option list was stripped.

The input arguments are:
***args***
the argument list
***options***
prefixed with a hyphen, e.g. '-x', and followed by a colon or ":" when an argument is required.
***long_options***
prefixed with two hyphens, e.g. --long-option, and followed by an equal sign or "=" when an argument is required.

2. ***Exception getopt.GetoptError***
is raised when an unrecognized option or none is found. The attributes msg and opt give the error message and related option.

Run this script with the following commands:
```python
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
```

### 3. test.py
#### sys.argv
```python
if __name__ == "__main__":
   main( sys.argv[1:] )
```
sys.argv is a list and sys.argv[1:] contains all the input arguments except the script name. The next part explains this more in detail.
##### Input Arguments
When input arguments are presented as follows:
```bash
$ python test.py -i in.txt -o out.txt
```
```python
sys.argv
['/home/aimldl/aimldl/temp/test.py', '-i', 'in.txt', '-o', 'out.txt']

sys.argv[0]
'/home/aimldl/aimldl/temp/test.py'

sys.argv[1]
'-i'

sys.argv[2]
'in.txt'

sys.argv[3]
'-o'

sys.argv[4]
'out.txt'

len( sys.argv )
5

sys.argv[1:]
['-i', 'in.txt', '-o', 'out.txt']
```
##### No input arguments
When input arguments are not presented as follows:
```bash
$ python test.py
```
```python
sys.argv
['/home/aimldl/aimldl/temp/test.py']

sys.argv[0]
'/home/aimldl/aimldl/temp/test.py'

sys.argv[1]
*** IndexError: list index out of range
```
#### getopt.getopt
This section explains the following part in test.py.
```python
def main( argv ):
  opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  ...
```
getopt.getopt takes argv as the input and returns opts & args.
```python
# Input
argv = ['-i', 'in.txt', '-o', 'out.txt']

# Output
opts
[('-i', 'in.txt'), ('-o', 'out.txt')]
args
argv = ['-i', 'in.txt', '-o', 'out.txt']
```
argv, opts & args are Python lists, but the elements of opts are tuples.
```python
# Python list
type( argv )
<class 'list'>

type( opts )
<class 'list'>

type( args )
<class 'list'>

# tuple
type( opts[0] )
<class 'tuple'>

type( opts[1] )
<class 'tuple'>
```
How opts works in the for loop is explained below.
```python
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
```
opts contains [('-i', 'in.txt'), ('-o', 'out.txt')] which is a list of tuples. Each tuple is split into opt and arg at each iteration of the for loop. 
```python
# First iteration in the for loop
opt
'-i'
arg
'in.txt'

# Second iteration in the for loop
opt
'-o'
arg
'out.txt'
```
As a result of each iteration,
```python
inputfile = arg
outputfile = arg
```
variable inputfile and outputfile stores the following strings.
```python
inputfile
'in.txt'
outputfile
'out.txt'
```
(EOF)
