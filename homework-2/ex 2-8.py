# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 07:54:10 2022

@author: gozde
"""

def fib(x):
    if x == 0 or x == 1:
        return x
    return fib(x - 1) + fib(x - 2)


fib_list = []
for i in range(20):
    fib_list.append(fib(i))

print(fib_list)

