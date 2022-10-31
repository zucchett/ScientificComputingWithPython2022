#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:25:34 2022

@author: alessandra
"""

#%%es08

def fibonacci(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
 
    
fib_list = [fibonacci(n) for n in range(20)]
print(fib_list)