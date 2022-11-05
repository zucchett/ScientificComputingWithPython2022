#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 16:53:07 2022

@author: alessandra
"""

#%% es07
# Integral of semicircle

import numpy as np

def Riemann(n):
    integral_sum = 0.
    h = 2./(n-1)
    for k in range(n):
        x_k = -1. + h*k
        integral_sum += h * np.sqrt(1 - x_k**2.)
    return integral_sum

print("Riemann integral value: ", Riemann(101))

import timeit

result_time_sec = timeit.timeit(lambda: Riemann(350000), number = 1)
print("Execution time of Riemann integral for N = 350000: ", result_time_sec, " sec")

result_time_min = timeit.timeit(lambda: Riemann(20000000), number = 1)
print("Execution time of Riemann integral for N = 20000000: ", result_time_min, " sec")
