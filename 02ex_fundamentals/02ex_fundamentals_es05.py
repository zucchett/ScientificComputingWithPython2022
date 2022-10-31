#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:46:11 2022

@author: alessandra
"""

#%%es05
# Write a Python program that sorts the following list of tuples using 
# a lambda function, according to the alphabetical order of the first 
# element of the tuple:
# Hint: use the method sort() and its argument key of the list data structure.

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = lambda t: t[0])

print(language_scores)

