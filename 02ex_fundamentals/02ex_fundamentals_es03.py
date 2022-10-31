#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:50:26 2022

@author: alessandra
"""


#%%es03
# Using the filter() hof, define a function that takes a list of words and an
# integer n as arguments, and returns a list of words that are shorter than n.

alist=["hello","world","python","filter","exercise"]

n = 5

def is_shorter(word):
    return len(word) <= n

print(list(filter(is_shorter,alist)))
