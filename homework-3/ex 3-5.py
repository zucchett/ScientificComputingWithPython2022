# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:51:42 2022

@author: gozde
"""

import math

#a
def quadratic1(a,b,c):
    r = math.sqrt(b*b - 4*a*c)
    return ((-b+r)/(2*a), (-b-r)/(2*a))

print("quadratic1 =", quadratic1(0.001,1000,0.001))

#b


def quadratic2(a,b,c):
    r = math.sqrt(b*b - 4*a*c)
    return (2*c/(-b-r), 2*c/(-b+r))
print("quadratic2 =", quadratic2(0.001,1000,0.001))


"""
quadratic1 = (-9.999894245993346e-07, -999999.999999)
quadratic2 = (-1.000000000001e-06, -1000010.5755125057)

in quadratic2, we see that the values are rounded. this happened because 
in the floats, the decimal place is limited, so it rounds the value.  
"""

#c
def quadratic(a,b,c):
    r = math.sqrt(b**2 - 4*a*c)
    return (2*c/(-b-r), (-b-r)/(2*a))
print("quadratic =", quadratic(0.001,1000,0.001))






