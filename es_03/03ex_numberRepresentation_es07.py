# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:58:16 2022

@author: Federico
"""

import math
import timeit

print("Known value of the integral: I =", math.pi/2, "\n")

def I(N):
    h = -1*N #change variable and go to integer range to remove roundoff errors in the sums along the x axis (which can lead to problems in sqrt math domain)
    integral = 0
    for k in range(N):
        h += 2
        integral += (2/N)*(math.sqrt((N*N)-h*h)/N)
    return integral
    
starttime = timeit.default_timer()
print("Numerical value (for N=100) =", I(100), "with computation time", timeit.default_timer() - starttime)
print("The difference from the known value is", I(100)-math.pi/2, "\n")
starttime = timeit.default_timer()
print("With few tests on the computation time one can see that if the code has to be run in less than a second, N can be increased to an approximate value of N=1570000")
print("Numerical value (for N=1570000) =", I(1570000), "with computation time", timeit.default_timer() - starttime, "\nThe difference between the known value is", I(1570000)-math.pi/2, "\n")

print("If instead the code has to be run in less than a minute, N can be increased to an approximate value of N=90000000")
print("Numerical value (for N=90000000) =", I(90000000), "with computation time", timeit.default_timer() - starttime, "\nThe difference from the known value is", I(90000000)-math.pi/2, "\n")