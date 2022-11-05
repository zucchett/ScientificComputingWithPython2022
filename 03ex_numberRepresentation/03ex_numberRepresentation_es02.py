# 2. 32-bit floating point number

# Write a function that converts a 32 bit binary string
# (for example, 110000101011000000000000) into a single
# precision floating point in decimal representation.
# Interpret the various bits as sign, fractional part of 
# he mantissa and exponent, according to the IEEE 754 reccommendations.


def string2float(astring):

    if len(astring) != 32:
        add_zero = 32- len(astring)
        # set length to 32
        for i in range(1, add_zero + 1):
            astring = "0" + astring
        
    # sign
    if astring[0] == '1':
        result = -1
        print("The sign is negative.")
    else:
        result = 1
        print("The sign is positive.")

    # exponent
    e = int(astring[1:9], 2)
    bias = int('01111111', 2)
    exp_n = e - bias
    print("The exponent is " + str(exp_n))

    # mantissa
    mantissa = 1 #int("1" + astring[9:32], 2)
    for m in range(1, 24):
        mantissa += ((float(astring[m+8]))/(2**m))
    print("The mantissa is " + str(mantissa))
        
    afloat = result * mantissa * (2**(exp_n))
    return afloat

ex_string = "110000101011000000000000"
ex_float = string2float(ex_string)
print("The floating point number is " + str(ex_float))

ex_string2 = "11111100101001001110001000111"
ex_float2 = string2float(ex_string2)
print("The floating point number is " + str(ex_float2))

# exercise done!

