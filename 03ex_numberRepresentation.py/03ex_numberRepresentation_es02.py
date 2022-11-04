#!/usr/bin/env python
# coding: utf-8

# In[3]:

#32-bit floating point number

string_binary = "110000101011000000000000"

def convertion(string):
    if string[0] == "1":
        sign = -1 
    else:
        sign = 1
    exp_bin = ""

    for i in range(1, 9):
        exp_bin = exp_bin + string[i]
    mantissa_bin = ""

    for i in range(9, 31):
        mantissa_bin = mantissa_bin + string[i]
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

print("Result: " + str(convertion("00000011111000000000000000000000")) + "\n")

print("Result: " + str(convertion("11000000101100000000000000000000")))


# In[ ]:




