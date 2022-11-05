# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:45:11 2022

@author: Federico
"""

F=[0,1]

for i in range(2,20):
    F.append(F[i-1]+F[i-2])
    
print(F)