# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 13:46:40 2022

@author: Ruben
"""

a=float(1)
i=0

while True:
    b=a
    a += 2**(-i)
    if a==b:
        break
    else:
        i += 1
    
print(float(2**(-i+1)))