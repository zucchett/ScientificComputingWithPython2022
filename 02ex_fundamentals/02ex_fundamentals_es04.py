#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:37:13 2022

@author: alessandra
"""

#%%es04 
# Write a function that takes the above dictionary and uses the map() 
# higher order function to return a list that contains the length of 
# the keys of the dictionary.

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def get_length(akey):
    return len(akey)

print(list(map(get_length,lang)))