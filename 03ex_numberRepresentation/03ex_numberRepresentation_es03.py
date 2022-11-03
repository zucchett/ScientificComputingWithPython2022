#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 23:10:40 2022

@author: alessandra
"""

#%%es03
# Write a program to determine the underflow and overflow limits (within a
# factor of 2) for floating point numbers on your computer.

# Hint: define two variables initialized to 1, and halve/double them for a
# sufficient amount of times to exceed the under/over-flow limits.

underflowLimit = 1
underList = []
for i in range(1100):
    underflowLimit = underflowLimit/2.
    underList.append(underflowLimit)
    #print("%2.5e" %underflowLimit)
    if underflowLimit == 0.:
        print("The underflow limit is: %2.5e" %underList[-2])
        break
    
from numpy import inf

overflowLimit = 1
overList = []
for i in range(1100):
    overflowLimit = overflowLimit*2.
    overList.append(overflowLimit)
    #print("%2.5e" %overflowLimit)
    if overflowLimit == inf:
        print("The overflow limit is: %2.5e" %overList[-2])
        break