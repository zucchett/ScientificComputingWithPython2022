# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:05:34 2022

@author: Federico
"""

def f(alist):
    alist_copy = []
    for i in range(len(alist)):
        alist_copy.append(alist[i])
    for j in range(5):
        alist_copy.append(j)
    return alist_copy

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) 