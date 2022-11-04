# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:36:41 2022

@author: Ruben
"""

x = 5

def f(alist):
    y= []
    for i in range(x):
        y.append(i)
    return alist+y

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) 