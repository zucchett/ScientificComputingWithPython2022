# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:25:31 2022

@author: Ruben
"""

def func(binary):
    b=binary
    m=1
    bias=127
    for i in range(22):
        m+=int(b[9+i])/(2**(i+1))
    e=int("0b"+b[1:9],2)
    x=((-1)**int(b[0]))*m*2**(e-bias)
    return x

binary="01000000010010010000111001010110"

print(func(binary))
    