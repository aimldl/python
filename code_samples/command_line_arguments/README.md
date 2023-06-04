##### aimldl > python3 > topics > command_line_arguments > README.md
  Rev.3: 2019-11-13 (Wed)
  Rev.2: 2019-11-07 (Thu)
  Rev.1: 2019-03-01 (Fri)
  Draft: 2018-11-08 (Thu)
TODO:
* Double-check & fix the examples in 2.Examples & the corresponding source codes.

# Command Line Arguments for Python
### 1. Basics
Read [tutorialspoint.com/README.md](tutorialspoint.com/README.md) to learn the basics. The following scripts show how to parse command line arguments with ***sys.argv*** and ***getopt.getopt***, respectively.
* [tutorialspoint.com/test-simple_example.py](tutorialspoint.com/test-simple_example.py) (for sys.argv)
* [tutorialspoint.com/test.py](tutorialspoint.com/test.py) (for sys.argv & getopt)

To learn how these scripts work in detail, refer to [tutorialspoint.com/README.md](#tutorialspoint.com/README.md).
### 2. Examples
Based on the two scripts from tutorialspoint.com, the following four scripts are created and explained below.

| File                                           | Section                                                  | sys.argv | getopt |
|------------------------------------------------|----------------------------------------------------------|----------|--------|
| [test-sys_argv.py](test-sys_argv.py)           | 2.1. Dealing with argc & argv                            | O        | X      |
| [test-getopt_simple.py](test-getopt_simple.py) | 2.2. Simple Option with -h or --help                     | O        | O      |
| [test-getopt_more.py](test-getopt_more.py)     | 2.3. Adding More Options to getopt                       | O        | O      |
| [test-getopt_full.py](test-getopt_full.py)     | 2.4. Get a Config, Input & Output File Names with getopt | O        | O      |

#### 2.1. Dealing with argc & argv (sys.argv)
Run the following script to learn how argc & argv work with respect to ***sys.argv***.
* [test-sys_argv.py](test-sys_argv.py)
```bash
  $ python test-sys_argv.py arg1 arg2 arg3
  argc=4
  argv=['test-sys_argv', 'arg1', 'arg2', 'arg3']
  file_name=test-sys_argv
  sys.argv[0]=test-sys_argv
  sys.argv[1]=arg1
  sys.argv[2]=arg2
    ...
  $
```
#### 2.2. Simple Option with -h or --help (sys.argv & getopt)
Run the following script with & without options to learn how ***getopt*** works from ***sys.argv***.
* [test-getopt_simple.py](test-getopt_simple.py)

Without an option,
```bash
    $ python test-getopt_simple.py
    argc=1
    argv=['test-getopt_simple.py']
    file_name=test-getopt_simple.py
    sys.argv[0]=test-getopt_simple.py
    opts=[]
    args=['test-getopt_simple.py']
    $
```
With short option -h,
```bash
    $ python test-getopt_simple.py -h
    argc=2
    argv=['test-getopt_simple.py', '-h']
    file_name=test-getopt_simple.py
    sys.argv[0]=test-getopt_simple.py
    sys.argv[1]=-h
    opts=[]
    args=['test-getopt_simple.py', '-h']
    $
```
With long option --help,
```bash
    $ python test-getopt_simple.py --help
    argc=2
    argv=['test-getopt_simple.py', '--help']
    file_name=test-getopt_simple.py
    sys.argv[0]=test-getopt_simple.py
    sys.argv[1]=--help
    opts=[]
    args=['test-getopt_simple.py', '--help']
    $
```

#### 2.3. Adding More Options to getopt (sys.argv & getopt)
Run the following script to learn about adding more options to getopt. This is a fully functioning script which can be used as a template to write your own command line argument parser.
* [test-getopt_more.py](test-getopt_more.py)

With short option -m,
```bash
$ python test-getopt_more.py -m option1
argc=3
argv=['test-getopt_more.py', '-m', 'option1']
file_name=test-getopt_more.py
sys.argv[0]=test-getopt_more.py
sys.argv[2]=option1
opts=[]
args=['test-getopt_more.py', '-m', 'option1']
$
```
With long option --my_option,
```bash
$ python test-getopt_more.py --my_option option2
argc=3
argv=['test-getopt_more.py', '--my_option', 'option2']
file_name=test-getopt_more.py
sys.argv[0]=test-getopt_more.py
sys.argv[2]=option2
opts=[]
args=['test-getopt_more.py', '--my_option', 'option2']
$
```
#### 2.4. Get a Config, Input & Output File Names with getopt (sys.argv & getopt)
From the command line, let's take in some file names with options as follows:

| Types       | Short Option   | Long Option          |
|-------------|----------------|----------------------|
| config file | -c example.cfg | --config example.cfg |
| input file  | -i input.txt   | --input input.txt    |
| output file | -o output.txt  | --output example.txt |

The following script can be used as a template to write your own command line argument parser.
* [test-getopt_full.py](test-getopt_full.py)

With short options,
```bash
$ python test-getopt_full.py -c example.cfg -i input.txt -o output.txt
argc=7
argv=['test-getopt_full.py', '-c', 'example.cfg', '-i', 'input.txt', '-o', 'output.txt']
file_name=test-getopt_full.py
sys.argv[0]=test-getopt_full.py
sys.argv[1]=-c
sys.argv[2]=example.cfg
  ...
opts=[]
args=['test-getopt_full.py', '-c', 'example.cfg', '-i', 'input.txt', '-o', 'output.txt']
$
```
With long options,
```bash
$ python test-getopt_full.py --config example.cfg --input input.txt --output output.txt
argc=7
argv=['test-getopt_full.py', '--config', 'example.cfg', '--input', 'input.txt', '--output', 'output.txt']
file_name=test-getopt_full.py
sys.argv[0]=test-getopt_full.py
sys.argv[1]=--config
sys.argv[2]=example.cfg
  ...
opts=[]
args=['test-getopt_full.py', '--config', 'example.cfg', '--input', 'input.txt', '--output', 'output.txt']
$
```
Just to make sure, both short and long options can be mixed together. For example,
```bash
$ python test-getopt_full.py -c example.cfg --input input.txt --output output.txt
argc=7
argv=['test-getopt_full.py', '-c', 'example.cfg', '--input', 'input.txt', '--output', 'output.txt']
file_name=test-getopt_full.py
sys.argv[0]=test-getopt_full.py
sys.argv[1]=-c
sys.argv[2]=example.cfg
  ...
opts=[]
args=['test-getopt_full.py', '-c', 'example.cfg', '--input', 'input.txt', '--output', 'output.txt']
```

### 3. Class Version of test-getopt_full.py
[command_line_arguments.py](#command_line_arguments.py) is the class version of [test-getopt_full.py](test-getopt_full.py). [command_line_arguments.py](#command_line_arguments.py) runs independently as follows:
```bash
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
```
It can be imported as a class.
* When it is located in the same directory that imports this class,
```python
import sys
from command_line_arguments import CommandLineArguments
  ...
if __name__ == '__main__':

    # Process the command line arguments
    cla = CommandLineArguments()
    argc = len( sys.argv )
    argv = sys.argv[1:]
    #cla.main( argc, argv )
    cla.main( argc, argv, debug=True )
      ...
```
* When it is located in sub-directory "python".
```python
from python.command_line_arguments import CommandLineArguments
```
You may use it as a template to parse your own command line arguments by changing the code.
```python
    def parse_arguments( self, argc, argv, debug=False ):
      ...
        # YOU MAY CHANGE THIS PART
        short_options = "hc:i:o:"                                 # Note : is used.
        long_options  = ["help", "config=", "input=", "output="]  # Note = is used.
        # YOU MAY CHANGE THIS PART
      ...
        # YOU MAY CHANGE THIS PART
        config_file = ''
        input_file  = ''
        output_file = ''
        # YOU MAY CHANGE THIS PART

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
```
#### Appendix: Further readings
* [GeeksforGeeks](https://www.geeksforgeeks.org/)
  * [Python | Set 6 (Command Line and Variable Arguments)](https://www.geeksforgeeks.org/python-set-6-arguments/)
  * [Command Line Interface Programming in Python](https://www.geeksforgeeks.org/command-line-interface-programming-python/)
  * [Python | How to Parse Command-Line Options](https://www.geeksforgeeks.org/python-how-to-parse-command-line-options/)

(EOF)
