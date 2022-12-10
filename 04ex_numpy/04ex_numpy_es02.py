#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:57:18 2022

@author: alessandra
"""

#%% ex02
# Find the outer product of the following vectors:

import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

# Use different methods to do this:

# Using the function outer in numpy
# Using a nested for loop or a list comprehension
# Using numpy broadcasting operations

outerProd_func = np.outer(u,v)
print("Outer product using function: ", '\n', outerProd_func)

p_nested_for = np.zeros((4,4))
for i in range(len(u)):
    for j in range(len(v)):
        val = u[i] * v[j]
        p_nested_for[(i, j)] = val
        
print("Outer product using nested for loop: ", '\n', p_nested_for)

p_list_compr = np.array([u[i] * v[j] for i in range(len(u)) for j in range(len(v))])

print("Outer product using list comprehension: ", '\n', p_list_compr.reshape(4,4))

p_broadcast = u.reshape(4,1) * v

print("Outer product using broadcasting operations: ", '\n', p_broadcast)