# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:21:21 2022

@author: Ruben
"""
import timeit

SETUP='''

def fibonacci(n):
    if n in range(1,3):
        return 1
    elif n==0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    


def loop_fibonacci(n):
    a=[0,1]

    for i in range(1,n):
        a.append(a[i]+a[i-1])
    
    return a[n]'''



time_1=timeit.timeit(stmt = "fibonacci(20)", setup = SETUP, number = 1)
print(time_1)

time_2=time_1=timeit.timeit(stmt = "loop_fibonacci(20)", setup = SETUP, number = 1)
print(time_2)



#The function defined using a loop is significantly faster