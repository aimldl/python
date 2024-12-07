# AttributeError from function in Module

## Problem

```python
AttributeError: module 'fibo' has no attribute 'fib2'
```

## Situation

I can not import a function in my custom module. For example, I have a module `fibo` in `fibo.py`.

```python
# fibo.py

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

When this module is imported, I can see function `fib`, but `fib2` can not be imported. Why?

```python
# In main.py
import fibo
Situation
fibo.fib(1000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

fibo.fib2(100)
# AttributeError: module 'fibo' has no attribute 'fib2'
```

The comments after the function calls are the output.

## Hint

> The dir() built-in function shows names defined inside a module.
>
> Source: [Python](https://www.python.org/) » [Documentation ](https://docs.python.org/3/index.html)» [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) » [6. Modules](https://docs.python.org/3/tutorial/modules.html) or my summary at [Import a Custom Module in Python](../how_to/import_a_custom_module.md).

Let's use the dir() function.

```python
import fibo

dir( fibo )
#['__builtins__',
# '__cached__',
# '__doc__',
# '__file__',
# '__loader__',
# '__name__',
# '__package__',
# '__spec__',
# 'fib']
```

Only `'fib'` is recognized as a name. 

Q: Why?

A: When the `fibo` module is loaded, only the `fib` function was in `fibo.py`. I've added the `fib2` function afterward.

> #### Note
>
> For efficiency reasons, each module is only imported once per interpreter session.  You must restart the interpreter if you change your modules. Use:
>
> ```python
> import importlib
> importlib.reload(modulename)
> ```
>
> Source: [Python](https://www.python.org/) » [Documentation ](https://docs.python.org/3/index.html)» [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) » [6. Modules](https://docs.python.org/3/tutorial/modules.html) or my summary at [Import a Custom Module in Python](../how_to/import_a_custom_module.md).

### Solution

The `fibo` module is reloaded and the problem is solved.

```python
import importlib
importlib.reload( fibo )

import fibo
dir( fibo )
#['__builtins__',
# '__cached__',
# '__doc__',
# '__file__',
# '__loader__',
# '__name__',
# '__package__',
# '__spec__',
# 'fib',
# 'fib2']
```

As the output is shown, the `fib2` function is visible as a name.