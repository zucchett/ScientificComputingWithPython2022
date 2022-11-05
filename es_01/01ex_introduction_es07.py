# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:41:52 2022

@author: Federico
"""

#for loop
a = []
for x in range(11):
    a.append(x**3)
print(a)

#list comprehension
l = [x**3 for x in range(11)]
print(l)