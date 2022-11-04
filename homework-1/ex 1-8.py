# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:46:51 2022

@author: gozde
"""

a = [(i, j) for i in range(3) for j in range(4)]
print(a)

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)