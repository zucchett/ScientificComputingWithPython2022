# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:41:43 2022

@author: Ruben
"""


def fibonacci(n):
    if n<3 and n>0:
        return 1
    elif n==0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
    
for i in range(20):
    print(fibonacci(i))