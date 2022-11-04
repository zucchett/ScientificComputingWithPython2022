# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 07:46:13 2022

@author: gozde
"""

def square(x):
    return x*x

def cube(x):
    return x*x*x


def power6(x):
    return square(cube(x))

x = 3
print(power6(x))

