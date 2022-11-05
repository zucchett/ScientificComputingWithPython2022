# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 19:31:01 2022

@author: Ruben
"""
        
x=input("Enter the frist variable value: ")
y=input("Enter the second variable value: ")

try:
    x = float(x)
    try:
        y = float(y)
        print(x+y)
    except:
        print("Impossible to perform the sum!")
except:
    try:
        y = float(y)
        print("Impossible to perform the sum!")
    except:
        print(x+y)