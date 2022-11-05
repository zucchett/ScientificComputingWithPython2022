#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:37:52 2022

@author: alessandra
"""

#%%es09


def fibonacci_rec(n):
    fib_list = []
    def fib_elem(n):
        if n <= 1:
            return n
        else:
            elem = fib_elem(n - 1) + fib_elem(n - 2)
            return elem
    for j in range(n):
        fib_list.append(fib_elem(j))
    return fib_list

def fibonacci_for(n):
    fib_list = []
    n0 = 0
    n1 = 1
    #n = 20
    fib_list.append(n0)
    fib_list.append(n1)
    for i in range(2,n):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list

def fibonacci_while(n_terms):
    count = 2
    n0 = 0
    n1 = 1
    fib_list = []
    fib_list.append(n0)
    fib_list.append(n1)
    while count < n_terms:
        n_i = n0 + n1
        fib_list.append(n_i)
        n0 = n1
        n1 = n_i
        count += 1
    return fib_list
        

print(fibonacci_rec(20))
print(fibonacci_for(20))
print(fibonacci_while(20))

import timeit

result_rec = timeit.timeit(lambda: fibonacci_rec(20), number = 1)
result_for = timeit.timeit(lambda: fibonacci_rec(20), number = 1)
result_while = timeit.timeit(lambda: fibonacci_rec(20), number = 1)

print("Recursive Fibonacci execution time --> ", result_rec)
print("For loop Fibonacci execution time --> ", result_for)
print("While Fibonacci execution time --> ", result_while)

if result_rec < result_for and result_rec < result_while:
    print("Recursive Fibonacci is faster")
elif result_for < result_while:
    print("For loop Fibonacci is faster")
else:
    print("While Fibonacci is faster")
