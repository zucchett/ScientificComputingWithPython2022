# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 17:37:06 2022

@author: Ruben
"""

a=[0,1]

for i in range(1,19):
    a.append(a[i]+a[i-1])

print(a)