#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:59:32 2022

@author: alessandra
"""

#%% es04
# Similarly to the previous exercise, write a program to determine the machine
# precision for floating point numbers.

# Hint: define a new variable by adding an increasingly smaller value and check
# when the addition starts to have no effect on the number.

l = []
for e in range(17):
    val = 1. + 1.0 * 10**-e
    l.append(val)
    if val != 1.:
        pass
    else:
        limit = (l[-2] - 1.) / 10.
        print("Machine precision: %2.20e" %limit)
        break
        