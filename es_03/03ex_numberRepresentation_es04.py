# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 20:21:24 2022

@author: Federico
"""

l = []

for exp in range(20):
    val = 1. + 1.0 * 10**-exp
    l.append(val)
    if val == 1.:
        limit = (l[-2] - 1.) / 10.
        print("Machine precision: ", limit)
        break