#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:46:54 2022

@author: alessandra
"""

#%% ex01
# Find the total mean, and the mean for each row and column of the
# following matrix:

import numpy as np
m = np.arange(12).reshape((3,4))

print(m)

mean_row = np.mean(m, axis = 1)
mean_col = np.mean(m, axis = 0)
mean_tot = np.mean(m)

print("Mean for each row: ", mean_row)
print("Mean for each column: ", mean_col)
print("Total mean: ", mean_tot)
