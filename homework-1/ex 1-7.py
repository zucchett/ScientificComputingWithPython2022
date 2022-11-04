# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:38:56 2022

@author: gozde
"""

#a
x = [i for i in range(0, 11)]
x_cubes=[]
for i in x:
    x_cubes.append(i**3)
print(x_cubes)

#b
x_cubes1 = [i**3 for i in x]
print(x_cubes1)