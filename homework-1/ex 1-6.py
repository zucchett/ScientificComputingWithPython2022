# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:33:31 2022

@author: gozde
"""

x = input("x= ")
y = input("y= ")

try:
    a = x + y
    print("x + y = ", a)
except:
    print("wrong input")