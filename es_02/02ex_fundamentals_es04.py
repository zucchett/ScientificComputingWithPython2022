# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:09:30 2022

@author: Federico
"""

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def key_len(dictionary):
    keys=[key for key in dictionary]
    return list(map(len, keys))

print(key_len(lang))