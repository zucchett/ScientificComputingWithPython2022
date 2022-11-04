# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 14:38:39 2022

@author: Ruben
"""
import sys
from decimal import Decimal

a=float(1)
c=float(1)
i=0
j=0


while True:
    d=c
    c=c/2
    if c==d:
        break
    else:
        j += 1
        
print("Underflow limit: %.2E" %float(2**(-j+1)))


while True:
    b=a
    a=a*2
    if b==a:
        break
    else:
        i += 1
print("Overflow limit: %.2E" %float(2**(i-1)))