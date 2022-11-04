# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:43:12 2022

@author: Federico
"""

start = ()
for a in range(100):
    for b in range(100):
        for c in range(100):
            if a**2+b**2 == c**2:
                start += ((a,b,c),)
print(start)