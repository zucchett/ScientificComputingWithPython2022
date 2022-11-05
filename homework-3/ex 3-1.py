# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 08:23:08 2022

@author: gozde
"""

def converter(number:int, type_num:str):
    num_bin = bin(number)
    num_hex = hex(number)
    if type_num == "bin":
        return num_bin
    elif type_num == "hex":
        return num_hex
    return number 

number = int(input("Enter an integer value: "))
print("Dec: "+str(converter(number, "dec")))
print("Bin: "+str(converter(number, "bin")))
print("Hex: "+str(converter(number, "hex")))