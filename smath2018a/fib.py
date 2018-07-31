"""
Fibonacci tools
"""
import sys


def fib(n):
    """
    Calculate a fibonacci number
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_cli():
    """
    Command line interface for fib
    """
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input('Enter an integer: '))
    print('fib({0}) = {1}'.format(n, fib(n)))
