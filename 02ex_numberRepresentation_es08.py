import timeit

def recursiveFibonacci(n):
    if n<2:
        return 1
    else:
        return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

(recursiveFibonacci(20))
'''
%timeit :2.21 ms ± 108 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
'''

