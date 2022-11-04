''' Created by Pedram on 11/03/2022 AD. '''

def extractSign(bin):
    return int(bin[0])

def extractExponent(bin):
    return int(bin[1 : 9], 2) 

def extractMantissa(bin):
    return int("1" + bin[9 : ], 2)

def binaryToFloatingPoint(bin):
    return (-1) ** extractSign(bin) * extractMantissa(bin) / (1 << (len(bin) - 9 - (extractExponent(bin) - 127)))

binaryNumber = "110000101011000000000000"  
print("Ans: ", binaryToFloatingPoint(binaryNumber)  )  