#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fibo.py   Fibonacci numbers module

Import this script with the following command.
  import fibo
"""

# Write Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Return Fibonacci series up to n
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    print('Hello! __main__ is called.')
    fib( int( sys.argv[1] ) )
