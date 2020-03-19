def fib(n):
    """ 
    Within the numseq package, create a module named `fib.py`. Within the fib module, define a function `fib(n)` that returns the nth Fibonacci number.  The first 10 terms of the Fibonacci sequence are 
    `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...]` recursive function
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
