#2. 32-bit floating point number (ex: 110000101011000000000000)

sign = 0
exponent = 0
bias = 127

def singlePrecisionFloating(binaryStr):
    sign = -1 ** int(binaryStr[0])
    exponent = int(binaryStr[1:9],2)
    mantissaStr = binaryStr[9:32]
    mantissa = 0
    mantissaBits = 1
    for bit in mantissaStr:
        if mantissaBits < 24:
            mantissa += int(bit)/2**mantissaBits
            mantissaBits+=1

    print('Sign:',sign)
    print('Exponent:',exponent)
    print('Mantissa:',mantissa)

    return sign * (1+mantissa) * (2 ** (exponent - bias))




binNumber = '11000010101100000000000000000000'

#print(len(binNumber))

print('Single Precision Floating Point Number:',singlePrecisionFloating(binNumber))
