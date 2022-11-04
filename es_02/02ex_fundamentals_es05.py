# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:09:26 2022

@author: Federico
"""

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = lambda x : x[0])

print(language_scores)