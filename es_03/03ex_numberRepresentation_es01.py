# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:50:41 2022

@author: Federico
"""

def typeconverter(in_number,out_repr): #input is a number in the right format (0b,0x,...)
    if out_repr=='bin':
        print(bin(in_number))
    elif out_repr=='hex':
        print(hex(in_number))
    elif out_repr=='dec':
        s=str(in_number)
        print(s)
    else: print("Invalid command")
    
typeconverter(0x100, 'bin')