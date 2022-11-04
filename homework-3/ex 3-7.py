# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:24:10 2022

@author: gozde
"""

from cmath import phase

#a
def semi_circle(x):
    return (1-(x**2)**1/2)

def integral(N, lower, upper, func):
    result = 0
    h = (upper-lower) / N
    
    for i in range(N):
        result = result + h * func(i)
    return phase(result)

    
N = 100

lower = -1
upper = 1

print(integral(N, lower, upper, semi_circle))

#b
import timeit

time = timeit.default_timer()
integral(N*10**3, lower, upper, semi_circle)
duration = timeit.default_timer() - time
print(duration)

"""
if N is multiplied by 10**3,
 it will run less than a second.
 """





