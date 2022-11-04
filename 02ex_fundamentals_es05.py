# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:38:12 2022

@author: Ruben
"""

"""Write a Python program that sorts the following list of tuples using a lambda function,
 according to the alphabetical order of the first element of the tuple:"""

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key=lambda x : x[0])


print(language_scores)