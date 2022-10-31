#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:31:19 2022

@author: alessandra
"""

x = 5

def f(alist):
    newlist = list(alist)
    for i in range(x):
        newlist.append(i)
    return newlist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed