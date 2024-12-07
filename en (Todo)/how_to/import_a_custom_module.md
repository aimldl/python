* Draft: 2020-05-07 (Thu)

# Import a Custom Module in Python

Google search: python custom library

## [Python](https://www.python.org/) » [Documentation ](https://docs.python.org/3/index.html)» [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) » [6. Modules](https://docs.python.org/3/tutorial/modules.html)

A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended. For instance,

fibo.py

```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Within a module, the module’s name (as a string) is available as the value of the global variable __name__. Using the module name you can access the functions:

```python
import fibo

fibo.__name__
#'fibo'

fibo.fib(1000)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

fibo.fib2(100)
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

fib = fibo.fib
fib(500)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 6.1. More on Modules

Variants of the import statement

```python
from fibo import fib, fib2
fib(500)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

```python
import fibo as fib
fib.fib(500)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

```python
from fibo import fib as fibonacci
fibonacci(500)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

#### Note

For efficiency reasons, each module is only imported once per interpreter session.  You must restart the interpreter if you change your modules. Use:

```python
import importlib
importlib.reload(modulename)
```

### 6.1.1. Executing modules as scripts

When you run

```bash
python fibo.py <arguments>
```

the `__name__` is set to `"__main__"`.

By adding this code at the end of your module, you can make the file usable as a script as well as an importable module.

```python
if __name__ == "__main__":
    import sys
    fib( int(sys.argv[1]) )
```

if the module is executed as the “main” file,

```bash
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

If the module is imported, the code is not run.

```python
>>> import fibo
>>>
```

### 6.1.2. The Module Search Path

When a module named `spam` is imported,

* the interpreter first searches for a built-in module with that name.
* If not found, it searches for `spam.py` in a list of directories given by the variable [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path).

[`sys.path`](https://docs.python.org/3/library/sys.html#sys.path) is initialized from these locations:

* The directory containing the input script (or the current directory when no file is specified).
* [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) (a list of directory names, with the same syntax as the shell variable `PATH`).
* The installation-dependent default.

After initialization, Python programs can modify [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path). 

> The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be loaded instead of modules of the same name in the library directory. This is an error unless the replacement is intended. See section [Standard Modules](https://docs.python.org/3/tutorial/modules.html#tut-standardmodules) for more information.
>
> TODO: read it again and summarize it.

#### Note

* In other words the directory containing the symlink is **not** added to the module search path.
* On file systems which support symlinks, the directory containing the input script is calculated after the symlink is followed.

[TODO]: summarize it. Start from

6.1.3. “Compiled” Python files

## [Python Programming](https://www.programiz.com/python-programming) > [Python Modules](https://www.programiz.com/python-programming/modules)

### What are modules in Python?

example.py

```python
# Python Module example

def add(a, b):
   """This program adds two
   numbers and return the result"""

   result = a + b
   return result
```

### How to import modules in Python?

```python
import example
example.add(4,5.5)
#9.5
```

### Import with renaming

I've changed the example from math to example.Draft: 2020-05-07 (Thu)

Using a Custom Library in Python
Google search: python custom library

```
import example as e
e.add(4,5.5)
#9.5
```

### Python from...import statement

I've changed the example from math to example.

```python
from example import add
add(4, 5, 6)
#9.5
```

### Import all names

Importing everything with the asterisk (*) symbol is not a good programming practice.

```python
from example import *
```

### Python Module Search Path

While importing a module, Python looks at several places. Interpreter first looks for a built-in module. Then(if built-in module not found), Python looks into a list of directories defined in sys.path. The search is in this order.

* The current directory.
* PYTHONPATH (an environment variable with a list of directories).
* The installation-dependent default directory.

```python
import sys
sys.path
```



The following is the output ran on Amazon SageMaker.

```python
['',
 '/home/ec2-user/anaconda3/envs/python3/lib/python36.zip',
 '/home/ec2-user/anaconda3/envs/python3/lib/python3.6',
 '/home/ec2-user/anaconda3/envs/python3/lib/python3.6/lib-dynload',
 '/home/ec2-user/anaconda3/envs/python3/lib/python3.6/site-packages',
 '/home/ec2-user/anaconda3/envs/python3/lib/python3.6/site-packages/IPython/extensions',
 '/home/ec2-user/.ipython']
```

### Reloading a module

The Python interpreter imports a module only once during a session. 

```python
>>> import my_module
This code got executed
>>> import my_module
>>> import my_module
```

Now if our module changed during the course of the program, we would have to reload it.

* One way to do this is to restart the interpreter. But this does not help much.
* We can use the `reload()` function inside the `imp` module to reload a module. 

```python
>>> import imp
>>> import my_module
This code got executed
>>> import my_module
>>> imp.reload(my_module)
This code got executed
<module 'my_module' from '.\\my_module.py'>
```

### The dir() built-in function

We can use the dir() function to find out names that are defined inside a module.

```python
>>> dir(example)
['__builtins__',
'__cached__',
'__doc__',
'__file__',
'__initializing__',
'__loader__',
'__name__',
'__package__',
'add']
```

```python
>>> import example
>>> example.__name__
'example'
```

```python
>>> a = 1
>>> b = "hello"
>>> import math
>>> dir()
['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']
```

