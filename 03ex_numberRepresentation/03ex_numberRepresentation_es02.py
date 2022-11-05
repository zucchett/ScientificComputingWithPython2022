# 2. 32-bit floating point number

# Write a function that converts a 32 bit binary string
# (for example, 110000101011000000000000) into a single precision
# floating point in decimal representation. Interpret the various bits
# as sign, fractional part of the mantissa and
# exponent, according to the IEEE 754 reccommendations.

# -------------------------------------- Code Begin-------------------------------------


def floatingPoint(binary):
    sign_bit = binary[0]
    exp_str = binary[1:9]
    mant_str = binary[9:] + '0'* (23-len( binary[9:]))
    ieee = 'SIGN : ' + str(sign_bit) + '|' + '  EXPONENT : '  + exp_str + '|' + '  MANTISSA : ' + mant_str
    print(ieee)
    return ((-1)**int(sign_bit)) *float('1.'+str(int(mant_str,2)))*2**(int(exp_str,2) - 127)
    
print(floatingPoint('110000101011000000000000'))



# -------------------------------------- Code End --------------------------------------
