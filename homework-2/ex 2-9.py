# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 07:56:34 2022

@author: gozde
"""

import timeit

def recursive_fibonacci(n):
    if n == 0 or n == 1: 
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def loop_fibonacci(n):
    fib = [0, 1]
    for i in range(20-2):
        fib.append(fib[-2] + fib[-1])
    return fib
 

starttime_loop = timeit.default_timer()
loop_fibonacci(20)
endtime_loop = timeit.default_timer() - starttime_loop
print("loop fibonacci: ", endtime_loop)

starttime_recursive = timeit.default_timer()
recursive_fibonacci(20)
endtime_recursive = timeit.default_timer() - starttime_recursive
print("recursive fibonacci: ", endtime_recursive)
print("the difference: ", (endtime_recursive/endtime_loop))
print("loop fibonacci is faster")
      