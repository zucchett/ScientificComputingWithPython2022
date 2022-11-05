def convert_binary(binary_String): #define function of convert_binary
    print("The entered binary is: ", binary_String)
    dec_Number = int(binary_String, 2)
    binary_Len = len(binary_String)#sign chenge to Index
    Newsign = 2 ** (binary_Len - 1)
    signShiftIndex = binary_Len - 1
    sign = (dec_Number & Newsign) >> signShiftIndex
    sign = 1 if sign == 0 else -1
    print("input Sign is: ", sign)
    exponentShiftIndex = binary_Len - 9 #exponent change to Index
    exponentMask = (2 ** 8 - 1) << exponentShiftIndex
    exponent = (dec_Number & exponentMask) >> exponentShiftIndex
    print("exponent is: %d, in binary: %s" % (exponent, bin(exponent)))
    mantissa_Bits = binary_Len - 9 #counting mantissa
    New_mantissa = (2 ** mantissa_Bits - 1)
    mantissaBin = dec_Number & New_mantissa
    list_of_m = [(mantissaBin & (2 ** (mantissa_Bits - i))) >> (mantissa_Bits - i)
                 for i in range(1, mantissa_Bits + 1)]
    frac_Mantissa = 0
    for i in range(mantissa_Bits):
        frac_Mantissa += list_of_m[i] / 2 ** (i + 1)
        i += 1
    mantissa = 1 + frac_Mantissa
    print("mantissa is: ", mantissa)
    floatNumber = sign * mantissa * 2 ** (exponent - 127)
    print("The converted result is: ", floatNumber)
# Example binary from the exercise file:
convert_binary("110000101011000000000000")
