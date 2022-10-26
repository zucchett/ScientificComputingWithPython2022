#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:45:56 2022

@author: alessandra
"""

#%%es04
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def count(string): # count characters in string
    output = {} # create dictionry
    string_lower = string.lower()
    for i in set(string_lower): # iterate over string
        output[i] = string_lower.count(i) # add key and value to dictionary
    return(output)

#print(count("hello"))
print(count(s1))
print(count(s2))