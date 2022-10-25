#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:49:08 2022

@author: alessandra
"""

#%%es09
my_pythagorean_tuple = tuple([(a, b, c) for a in range(1,100) for b in range(1,100) for c in range(1,100) if a**2. + b**2. == c**2.])
print(my_pythagorean_tuple)