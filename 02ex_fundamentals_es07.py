# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 13:00:17 2022

@author: Ruben
"""

def hello(func):
    def wrapper(x):
        print("Hello World!")
        return func(x)
    return wrapper
        

@hello
def square(x):
    return x*x


print(square(8))