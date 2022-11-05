#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:49:58 2022

@author: alessandra
"""

#%%es11 Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops
def fibonacci0(n):
    fib_list = []
    n0 = 0
    n1 = 1
    #n = 20
    fib_list.append(n0)
    fib_list.append(n1)
    for i in range(2,n):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list

def fibonacci1(n_terms):
    count = 2
    n0 = 0
    n1 = 1
    fin_list = []
    fin_list.append(n0)
    fin_list.append(n1)
    while count < n_terms:
        n_i = n0 + n1
        fin_list.append(n_i)
        n0 = n1
        n1 = n_i
        count += 1
    return fin_list
        
print(fibonacci0(20))
print(fibonacci1(20))