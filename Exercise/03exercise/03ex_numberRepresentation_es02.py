#2. 32-bit floating point number:
def convertToFloat(b):
    s= b[0]             #Sign bit
    s = int(s)
    print("sign bit: ", s)
    exp = b[1:9]        #Exponent bits
    print("exponent bits: ", exp)
    exp= int(exp,2)     #Convert binary to decimal for getting the exponent No
    print("exponent number is: ", exp)
    f = b[9:32]         #Fraction bits
    print("Fraction bits: ", f)
    ans=0
    for i in range(len(f)):   #Fraction exponent
        if f[i] == '1':
            ans += 1/(2**i)
    f = ans
    print("fraction number is: ", f)
    floatNo = (-1)**s * (1 + f) * 2**(exp - 127)
    return floatNo

binaryNo= "11000010101100000000000000000000" #32bits
print("The float number is: ", convertToFloat(binaryNo))
