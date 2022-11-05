#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 16:38:14 2022

@author: alessandra
"""

#%% es07

def func(x):
    return x * (x-1.)

def derivative(delta):
    x = 1.
    return (func(x + delta) - func(x)) / delta

def anDerivative():
    x = 1.
    return 2.*x-1.

print("Derivative using definition --> ", derivative(10.**-2.))
print("Analytical derivative --> ", anDerivative())

print("Accuracy for different deltas: ")
for i in range(2,16,2):
    d = 10.**-i
    print(derivative(d)-anDerivative())
    
