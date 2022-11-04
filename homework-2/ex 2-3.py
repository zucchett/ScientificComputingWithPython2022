# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 07:32:46 2022

@author: gozde
"""

def shorter(list1,n):
    return list(filter(lambda list1: len(list1) < n, list1))

list1 = ["Python", "Java", "Cpluplus", "Hello", "World", "Polygon"]
print(str(shorter(list1, 7))) 