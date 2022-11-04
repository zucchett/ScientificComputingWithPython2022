# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 12:35:47 2022

@author: Ruben
"""

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

b = [(i,j) for i in range(3) for j in range(4)]
print(b)