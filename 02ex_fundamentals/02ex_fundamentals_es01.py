# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:57:18 2022

@author: Tullia
"""
x = 5

def f(alist):
    alist = []
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has not been changed

