#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:48:43 2022

@author: alessandra
"""

#%%es08
a = []
for i in range(3): # for loop
    for j in range(4):
        a.append((i, j))
print(a)

list_1 = [(i,j) for i in range(3) for j in range(4)] # list comprehension
print(list_1)