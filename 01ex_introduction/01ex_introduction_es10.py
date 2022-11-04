# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:51:00 2022

@author: Ruben
"""
import math

a=[]
x=[]

i=0
print("\n Type stop when you want to terminate vector formatting \n")
while True:
    x=input("Enter the %d ° component of the vector: " % (len(a)+1) )
    if x == "stop":
        break
    try:
        a.append(float(x))
    except:
        print("\n Please enter a number!\n")
    i += 1

b=[a[i]**2 for i in range(len(a))]
r=math.sqrt(sum(b))

c=[a[i]/r for i in range(len(a))]


print("\n The normalized vector reads \n", c)