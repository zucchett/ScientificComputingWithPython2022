#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 22:49:38 2022

@author: alessandra
"""

#%%es02
# Write a function that converts a 32 bit binary string (for example, 
# 110000101011000000000000) into a single precision floating point in decimal 
# representation. Interpret the various bits as sign, fractional part of the 
# mantissa and exponent, according to the IEEE 754 reccommendations.

def mantissaValue(mant):
    power_of_two = -1
    mantissa_value = 0
    for i in mant:
        mantissa_value += (int(i) * pow(2, power_of_two))
        power_of_two -= 1
    return (mantissa_value + 1)

def convertToSinglePrecision(num):
    
    """ Convert 32 bit binary string into single precision
    floating point in decimal representation.
    
    x_float = (-1)**s*1.f*2**(e-bias)"""
    
    n = str(num)
    
    sign_bit = int(n[0])
    
    exponent = int(n[1:9], 2)
    
    mantissa = n[10:]
    
    mantissa_val = mantissaValue(mantissa)
    
    number = pow(-1, sign_bit) * mantissa_val * pow(2, exponent - 127)
    
    return number

print(convertToSinglePrecision(110000101011000000000000))
    
    
    
        