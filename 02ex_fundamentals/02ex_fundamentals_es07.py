#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:10:21 2022

@author: alessandra
"""

#%%es07
#Write a decorator named hello that makes every wrapped function 
#print “Hello World!” each time the function is called.

#The wrapped function should look like:

#@hello
#def square(x):
#    return x*x

def hello(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        print("Hello World!")
    return wrapper

@hello
def square(x):
    print(x*x)

square(2)
