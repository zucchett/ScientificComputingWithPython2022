#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:41:10 2022

@author: alessandra
"""

#%% ex03
# Create a 10 by 6 matrix of float random numbers, distributed between
# 0 and 3 according to a flat distribution.

# After creating the matrix, set all entries <0.3 to zero using a mask.

import numpy.random as npr

arrRnd = npr.uniform(0.,3.,(10,6))

print("Matrix of float random numbers:",'\n', arrRnd)

arrRnd[arrRnd < 0.3] = 0.

print("Filtered array:",'\n', arrRnd)
