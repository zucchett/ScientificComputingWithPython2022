#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 16:05:09 2022

@author: alessandra
"""

#%% ex07
# Compute the prime numbers in the 0-N (start with N=99) range with
# a sieve (mask).

# Constract a shape (N,) boolean array, which is the mask
# Identify the multiples of each number starting from 2 and set
# accordingly the corresponding mask element
# Apply the mask to obtain an array of ordered prime numbers
# Check the performances (with timeit); how does it scale with N?
# Implement the optimization suggested in the sieve of Eratosthenes

import numpy as np
import timeit


def primeArray0():
    boolArray = np.ones((100,), dtype = bool)
    nMax = int(np.sqrt(len(boolArray)))
    
    for j in range(len(boolArray)):
        for i in range(2, nMax):
            if j % i == 0:
                if j > i:
                    boolArray[j] = False
    
    boolArray[:2] = 0

    primeArray = np.nonzero(boolArray)
    
    return primeArray
   
print("Prime numbers (1st method): ", '\n', primeArray0())

result_0 = timeit.timeit(lambda: primeArray0(), number = 1)
print("Execution time: ", result_0)

"""Sieve of Eratosthenes"""

def primeArrayErat():
    is_prime = np.ones((100,), dtype=bool)

    is_prime[:2] = 0

    nmax = int(np.sqrt(len(is_prime)))
    for i in range(2, nmax):
        is_prime[2*i::i] = False

    primeArrayErat = np.nonzero(is_prime)
    
    return primeArrayErat

print("Prime numbers (Eratosthenes):",'\n', primeArrayErat())
result_E = timeit.timeit(lambda: primeArrayErat(), number = 1)
print("Execution time (sieve of Eratosthenes): ", result_E)
