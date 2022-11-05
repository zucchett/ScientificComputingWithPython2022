# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:32:44 2022

@author: Ruben
"""

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
"""Write a function that takes the above dictionary and uses the map() higher order function 
to return a list that contains the length of the keys of the dictionary."""

def count(key):
    n=len(key)
    return n

def func(dict):
    keys_len=list(map(count, dict.keys()))
    return keys_len

print(func(lang))
