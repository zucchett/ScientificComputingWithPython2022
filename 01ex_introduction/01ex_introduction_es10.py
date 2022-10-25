#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:49:33 2022

@author: alessandra
"""

#%%es10
import numpy as np

def normalize(n_dim_tuple):
    n = 0
    for i in range(len(n_dim_tuple)):
        n  += n_dim_tuple[i]**2.
    return np.sqrt(n)

a_tuple = (2,4,6,8,10)
print(normalize(a_tuple))