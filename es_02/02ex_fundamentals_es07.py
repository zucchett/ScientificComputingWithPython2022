# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:11:08 2022

@author: Federico
"""

def hello(func):
    def wrapper(x):
        print("Hello World!")
        func(x)
    return wrapper

@hello
def square(x):
    print(x*x)
    
square(7)