# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 11:34:06 2022

@author: Ruben
"""
import math

a=[]

for x in range(11):
    a.append(x**3)
    x += 1
    
print(a)

b= [x**3 for x in range(11)]

print(b)