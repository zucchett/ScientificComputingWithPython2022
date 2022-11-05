# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:10:01 2022

@author: gozde
"""

#a
def func(x):
    return x*(x-1)

def derfunc(func, x, delta = 10**(-2)):
    return(func(x+delta) - func(x)) / delta

x = 1
result = derfunc(func, x)
print(result)


#b
deltas = [10**(-4), 10**(-6), 10**(-8), 10**(-10), 10**(-12), 10**(-14)]

for i in deltas:
    print("Derivative on ", i , " = " , derfunc(func, x, i))
