#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:34:35 2022

@author: alessandra
"""

#%%es01
# Write a function that converts numbers among the bin, dec, and hex 
# representations (bin<->dec<->hex). Determine the input type in the 
# function, and pass another argument to choose the output representation.

def convertTo():
    user_type = input("Decide input data type: [type <bin>,<dec>,<hex>] ")
    user_n = input("Type the number: ")
    user_out = input("Convert to : [type <bin>,<dec>,<hex>] ")
    if user_type == "bin" or user_type == "BIN": # if binary
        n = int(user_n, 2)
        print("Binary representation of number", bin(n))
        if user_out == "dec" or user_type == "DEC":
            out = int(n)
            print("Decimal representation = ", out)
        elif user_out == "hex" or user_type == "HEX":
            out = hex(n)
            print("Hexadecimal representation = ", out)
        
    if user_type == "dec" or user_type == "DEC": # if decimal
        n = int(user_n)
        print("Decimal representation of number", n)
        if user_out == "bin" or user_type == "BIN":
            out = bin(n)
            print("Binary representation = ", out)
        elif user_out == "hex" or user_type == "HEX":
            out = hex(n)
            print("Hexadecimal representation = ", out)
            
    if user_type == "hex" or user_type == "HEX": #if hexadecimal
        n = int(user_n, 16)
        print("Hexadecimal representation of number", hex(n))
        if user_out == "bin" or user_type == "BIN":
            out = bin(n)
            print("Binary representation = ", out)
        elif user_out == "dec" or user_type == "DEC":
            out = int(n)
            print("Decimal representation = ", out)
    
convertTo()
