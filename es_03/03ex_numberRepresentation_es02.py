# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:52:56 2022

@author: Federico
"""

def converter(x):
    s = str(x)
    
    if len(s) == 32: #check that the binary string has 32 bit

        exponent = -127 
        for i in range(1,9):
            exponent += int(s[i])*2**(8-i) #extract the exponent
        
        mantissa = 1
        for i in range(9,len(s)):
            mantissa += int(s[i])*2**(8-i) #extract the mantissa
          
        number_10 = ((-1)**int(s[0]))*mantissa*(2**(exponent)) #resum the number(10) according to the IEEE 754 reccommendations
        
        return number_10
            
    else:
        print("Invalid string (it must have 32 bits!)")
        
print(converter(11000000101110101000000000000000)) #test: -5,828125 