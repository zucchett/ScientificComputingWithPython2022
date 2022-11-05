# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:43:58 2022

@author: Federico
"""

import math 

v = (1, 23.45, -2) #define your N dimensional vector

normsq = 0
for i in range(len(v)):
    normsq += v[i]**2
    
N = math.sqrt(normsq) #compute the norm of your vector
print("Vector v =", v, "has norm N =",N)

b = ()
for i in range(len(v)):
    b += ((v[i]/N),) #rescale the entries by the norm

print("The renormalized vector is v' =", b)