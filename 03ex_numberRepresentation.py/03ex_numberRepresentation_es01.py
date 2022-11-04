#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Number representation

def converter_num(x:int):

    bin_num = bin(x)
    hex_num = hex(x)
    
    print("Binary representation: " + str(bin_num))
    print("Hexadecimal representation: " + str(hex_num))
    print('Decimal representation of', bin_num, ':', int(bin_num, 2))
    print('Decimal representation of', hex_num, ':', int(hex_num, 16))

no = int(input("Enter an integer: "))
converter_num(no)


# In[ ]:




