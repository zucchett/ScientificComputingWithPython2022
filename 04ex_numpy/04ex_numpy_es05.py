#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:25:31 2022

@author: alessandra
"""

#%% ex05
# Create a matrix that shows the 10 by 10 multiplication table.

# Find the trace of the matrix
# Extract the anti-diagonal matrix (this should be
# array([10, 18, 24, 28, 30, 30, 28, 24, 18, 10]))
# Extract the diagonal offset by 1 upwards (this should be
# array([ 2,  6, 12, 20, 30, 42, 56, 72, 90]))

import numpy as np

u = np.array(np.arange(1,11,1))
v = np.array(np.arange(1,11,1))

moltTable = np.array([u[i] * v[j] for i in range(len(u)) for j in range(len(v))]).reshape(10,10)
print(moltTable)

trace = np.trace(moltTable)
print("The trace is: ", trace)

antiDiag = np.diag(np.fliplr(moltTable))
print("The anti-diagonal is:", antiDiag)

diagOff = np.diag(moltTable, k=1)
print("The diagonal offset by 1 upwads is: ", diagOff)

