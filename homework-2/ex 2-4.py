# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 07:41:35 2022

@author: gozde
"""

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}



def func1(words):
    key_list = words.keys()
    keylen_list = list(map(len, key_list))
    return keylen_list
    
keylen_list = func1(lang)
print(keylen_list)
