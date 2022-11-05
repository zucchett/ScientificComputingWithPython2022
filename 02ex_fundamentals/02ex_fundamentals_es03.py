# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:03:15 2022

@author: Ruben
"""


w_list = ["ciao", "mamma", "cane", "amicomio", "ah"]


def filtering(alist, n):
    def func(word):
        return True if len(word) < n else False
    newlist=list(filter(func, alist))
    
    return newlist
    

print(filtering(w_list, 6))