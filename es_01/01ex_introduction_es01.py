# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:32:44 2022

@author: Federico
"""

i=1
t=()
while i<=100:
    if ((i%3)==0 and (i%5)!=0):
        print("Hello")
        t+=("Python",)
    elif ((i%3)!=0 and (i%5)==0):
        print("World!")
        t+=("Works",)
    elif ((i%3)==0 and (i%5)==0):
        print("Hello World!")
        t+=("Python Works!",)
    else: print(i);t+=(i,)
    i+=1
print(t)