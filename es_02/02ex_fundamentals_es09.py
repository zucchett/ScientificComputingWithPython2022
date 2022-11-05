# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:22:35 2022

@author: Federico
"""
import timeit

def recursiveFibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return recursiveFibonacci(n-1)+recursiveFibonacci(n-2)
   
for n in range(20):
    print(n, recursiveFibonacci(n))
start = timeit.default_timer() 
recursiveFibonacci(19) #measure computation time
print("computation time for recursive Fibonacci: ", timeit.default_timer() - start)

start = timeit.default_timer()     
F=[0,1]
for i in range(2,20):
    F.append(F[i-1]+F[i-2]) #measure computation time
print("computation time for loop Fibonacci: ", timeit.default_timer() - start)
print(F)    