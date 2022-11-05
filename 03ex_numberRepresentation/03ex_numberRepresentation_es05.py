# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 00:50:45 2022

@author: Ruben
"""

import math

def res_1(a,b,c):
    x_1=(-b-math.sqrt(b**2 - 4*a*c))/(2*a)
    x_2=(-b+math.sqrt(b**2 - 4*a*c))/(2*a)
    x=[x_1,x_2]
    return x

def res_2(a,b,c):
    x_1=2*c/(-b+math.sqrt(b**2 - 4*a*c))
    x_2=2*c/(-b-math.sqrt(b**2 - 4*a*c))
    x=[x_1,x_2]
    return x

#the first solution of res_1 is obtained through a subtraction between two nearby floating-point
#numbers, which is ill-conditioned. The same happens for the second solution
#of res_2. 


def res_def(a,b,c):
    x_1=(-b-math.sqrt(b**2 - 4*a*c))/(2*a)
    x_2=2*c/(-b-math.sqrt(b**2 - 4*a*c))
    x=[x_1,x_2]
    return x


print(res_1(0.001,1000,0.001))
print(res_2(0.001,1000,0.001))
print(res_def(0.001,1000,0.001))