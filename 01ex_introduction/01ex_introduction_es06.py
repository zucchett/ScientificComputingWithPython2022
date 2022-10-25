#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:46:44 2022

@author: alessandra
"""

#%%es06
a = input("Type something and press <Enter>: ")
b = input("Type something and press <Enter>: ")

try:
    a = float(a)
except:
    try:
        b = int(b)
    except:
        pass
try:
    b = float(b)
except:
    try:
        a = int(a)
    except:
        pass

try:
    print(a + b)
except:
    print("Error: invalid input")
               