# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:48:38 2022

@author: Ruben
"""

import math

while True:
    try:
        x,y=input("Enter the first two values, separated by a whitespace: ").split()
        x,y=float(x),float(y)
        a,b=input("Enter the second two values, separated by a whitespace: ").split()
        a,b=float(a),float(b)
        break
    except ValueError: print("\nValues have not been entered correctly!\n")

r=math.sqrt((x-a)**2+(y-b)**2)

print(r)



