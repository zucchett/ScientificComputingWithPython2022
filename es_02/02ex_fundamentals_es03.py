# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:08:10 2022

@author: Federico
"""

n = int(input("I'll select the words with length < n: what is n? (write an integer) \n"))
def short(x):
    return len(x)<n

def length_filter(y): 
    return filter(short, y)

print(list(length_filter(["up", "down", "charm", "strange", "top", "bottom"]))) #example