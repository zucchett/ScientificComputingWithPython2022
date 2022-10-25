#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:42:38 2022

@author: alessandra
"""

#%%es01
a = "Hello"
b = "World"
c = "Python"
d = "Works"

my_list = []

for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0: # check if multiple of 3 and 5
        print(a+b)
        my_list.append(c+d)
    elif x % 3 == 0: # check if multiple of 3
        print(a)
        my_list.append(c)
    elif x % 5 == 0: # check if multiple of 5
        print(b)
        my_list.append(d)
    else: # all other cases
        print(x)
        my_list.append(x)
        
def convert_to_tuple(list): # convert to tuple
    return tuple(list) 

print(convert_to_tuple(my_list))
