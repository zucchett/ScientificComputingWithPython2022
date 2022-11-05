def convert_binary(binaryString):
    print("The entered binary is: ", binaryString)
    decNumber = int(binaryString, 2)
    binaryLen = len(binaryString)

    signMask = 2 ** (binaryLen - 1)
    signShiftIndex = binaryLen - 1
    sign = (decNumber & signMask) >> signShiftIndex
    sign = 1 if sign == 0 else -1
    print("Sign of the input is: ", sign)

    exponentShiftIndex = binaryLen - 9
    exponentMask = (2 ** 8 - 1) << exponentShiftIndex
    exponent = (decNumber & exponentMask) >> exponentShiftIndex
    print("exponent is: %d, in binary: %s" % (exponent, bin(exponent)))

    mantissaBitsCount = binaryLen - 9
    mantissaMask = (2 ** mantissaBitsCount - 1)
    mantissaBin = decNumber & mantissaMask
    list_of_m = [(mantissaBin & (2 ** (mantissaBitsCount - i))) >> (mantissaBitsCount - i)
                 for i in range(1, mantissaBitsCount + 1)]
    fractionalOfMantissa = 0
    for i in range(mantissaBitsCount):
        fractionalOfMantissa += list_of_m[i] / 2 ** (i + 1)
        i += 1
    mantissa = 1 + fractionalOfMantissa
    print("mantissa is: ", mantissa)
    floatNumber = sign * mantissa * 2 ** (exponent - 127)
    print("The float number is: ", floatNumber)
    print("------------------End of Function ---------------------")


# Example binary from the exercise file:
convert_binary("110000101011000000000000")

# Example binaries from the lecture file:
convert_binary("00000011111000000000000000000000")
convert_binary("11000000101100000000000000000000")

# Although I spent around 2 hours on this exercise, I managed to fully understand the concept of Masking and
# shifting, and floating point numbers
