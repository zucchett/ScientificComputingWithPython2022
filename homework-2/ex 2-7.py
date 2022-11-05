# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 07:53:49 2022

@author: gozde
"""

def hello(func):
    def wrapper(x):
        print("HelloWorld")
        return func(x)
    return wrapper

@hello
def square(x):
    return x*x

print(square(3))