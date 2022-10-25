#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:48:16 2022

@author: alessandra
"""

#%%es07
list_a = []
for i in range(11): # list using for loop
    list_a.append(i**3.)


list_b = [x**3. for x in range(11)] # list using list comprehension

print(list_a)
print(list_b)