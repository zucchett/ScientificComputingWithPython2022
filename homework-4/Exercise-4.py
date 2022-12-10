# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:48:01 2022

@author: gozde
"""
"""
Exercise-4: Numpy

"""

import numpy as np

#1 Reductions
m = np.arange(12).reshape((3,4))
print(m)

print("Total mean: ", np.mean(m))
print("Mean of rows", np.mean(m, axis=1))
print("Mean of columns", np.mean(m, axis=0))

#2 Outer Product
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

#2.1
print("with function outer: \n", np.outer(u, v))

#2.2
outer_product = []
for i in range(len(u)):
    for j in range(len(v)):
        x = (u[i]*v[j])
        outer_product.append(x)
                  
print("with nested for loop: \n", outer_product)

#2.3
from numpy import newaxis
a = (u[:, newaxis] * v)
print("with numpy broadcasting: \n ", a)

#3 Matrix masking
a = np.linspace(0,3,60).reshape(10,6)
print(a)

mask = (a < 0.3) 
a[mask] = 0
print("filtered a: \n", a)

#4 Trigonometric Functions
from math import pi
a = np.linspace(0, (2*pi+1), 100)
print(a)

print("\n every 10th element: \n ", a[::10])
print("\n reverse of the array a: ", a[::-1])

result = np.absolute(np.cos(a) - np.sin(a))
mask = (result < 0.1) 
filtered_result = result[mask]

print("\n absolute difference: \n",result)
print("\n absolute difference smaler than 0.1: \n",filtered_result)

#5 Matrices
ns = np.arange(1, 11)
m = ns[:, None] * ns[None, :]
print(m)
print("Trace of the matrix: \n", m.trace())
print("Extracted anti-diagonal matrix: \n", np.flipud(m).diagonal())
print("Extracted diagonal offset by 1 upwards: \n", m.diagonal(offset=1))

#6 Broadcasting
positions = np.array([ 0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
distance = np.abs(positions - positions[:, np.newaxis])
print("distances among each city: \n", distance)
print("mile to km: \n", distance/1.609344)

#7 Prime numbers sieve
from math import pow, ceil
import timeit

def prime_numbers_sieve(n):                  
    N = [True for i in range(n+1)]
    N[1] = False
    prime_numbers = []
    for i in range(2, ceil(pow(n, 0.5))+1):
        if N[i]:
            for j in range(i*i, n+1, i):
                N[j] = False
    for i in range(2, n+1):
        if N[i]:
            prime_numbers.append(i)
    return prime_numbers

n = 999
print(prime_numbers_sieve(n))
time = timeit.timeit('prime_numbers_sieve(n)', globals=globals(), number=99)
print("time: ", time)
#with n=99, time=0.004764099999874816
#with n=999, time=0.021178499999905398
#time increases as n increases

#8 Diffusion using random walk
walkers = 1000
steps = 200
x = np.random.randint(0,2,(walkers,steps))
x[x == 0] = -1
print("walkers x steps  with values -1 or 1: \n", x)

walking_distances = x.sum(axis = 1)
print('the walking distances: \n',walking_distances)

walking_distances_squared = np.square(walking_distances)

mean_squared_distances = np.mean( np.cumsum(x, axis = 1)**2 , axis = 0)
print('the mean: \n',mean_squared_distances)

