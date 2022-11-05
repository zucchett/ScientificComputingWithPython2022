# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:12:28 2022

@author: Federico
"""

def recursiveFibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursiveFibonacci(n-1)+recursiveFibonacci(n-2)
    
for n in range(20):
    print(n, recursiveFibonacci(n))
    