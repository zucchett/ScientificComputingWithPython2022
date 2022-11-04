# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 00:07:35 2022

@author: gozde
"""

def fibonacci(n):
    f = [1,1]
    x = 2
    while x <= n:
        f.append(f[x - 1] + f[x - 2])
        x = x + 1
    return f

print(str(fibonacci(19)))