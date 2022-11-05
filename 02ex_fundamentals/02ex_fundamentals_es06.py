#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:03:06 2022

@author: alessandra
"""

#%%es06

def square(x):
    return x*x

def cube(x):
    return x*x*x

def sixth_power0(x):
    return cube(square(x))

def sixth_power1(x):
    return square(cube(x))

print(sixth_power0(2))
print(sixth_power1(2))