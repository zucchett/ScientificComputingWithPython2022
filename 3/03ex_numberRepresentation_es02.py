# 2. 32-bit floating point number

# Write a function that converts a 32 bit binary string 
# (for example, `110000101011000000000000`) into a single precision floating point 
# in decimal representation. Interpret the various bits as sign, fractional part 
# of the mantissa and exponent, according to the IEEE 754 reccommendations.

def f(float_number:str):
    sign = -1 if float_number[0] == "1" else 1
    exponent_binary = ""
    for i in range(1, 9):
        exponent_binary = exponent_binary + float_number[i]
    mantissa_binary = ""
    for i in range(9, 31):
        mantissa_binary = mantissa_binary + float_number[i]
    exponent = int(exponent_binary, 2)
    mantissa = 1

    counter = 1
    for i in mantissa_binary:
        mantissa = mantissa + (int(i) / 2**counter) 
        counter = counter + 1
    mantissa = mantissa * sign
    print("Sign: "+str(sign))
    print("Exponent: "+str(exponent))
    print("Mantissa: "+str(mantissa))
    return mantissa * (2 ** (exponent - 127))

print("Result: "+str(f("00000011111000000000000000000000")))
print()
print("Result: "+str(f("11000000101100000000000000000000")))