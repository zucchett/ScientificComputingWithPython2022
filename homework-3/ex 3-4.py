# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 08:53:31 2022

@author: gozde
"""

a = 1
for i in range(10000):
    x = a / 10
    if x != a:
        a = x
    else:
        print("decimal of precision = ", i)
        break