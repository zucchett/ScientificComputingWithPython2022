# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 08:27:14 2022

@author: gozde
"""

binary_string = "110000101011000000000000"

def convertfloat(x):
    if x[0] == "1":
        sign = -1
    else:
        sign = 1
    exp_bin = ""
    
    for i in range(1,9):
        exp_bin = exp_bin + x[i]
    mantissa_bin = ""
    
    for i in range(9,31):
        mantissa_bin = mantissa_bin + x[i]
    exp = int(exp_bin, 2)
    mantissa = 1
    
    counter = 1
    for i in mantissa_bin:
        mantissa = mantissa + (int(i) / 2**counter) 
        counter = counter + 1
    mantissa = mantissa * sign

    print("Sign: " + str(sign))
    print("Exponent: " + str(exp))
    print("Mantissa: " + str(mantissa))
    return mantissa * (2**(exp-127))

print("Result: ", convertfloat("00000011111000000000000000000000"))

