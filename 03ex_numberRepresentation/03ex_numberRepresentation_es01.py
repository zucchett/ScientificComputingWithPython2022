''' Created by Pedram on 11/02/2022 AD. '''

def convertToDecimal(number, base):
    return int(number, base)

def convertToHexaDecimal(number):
    return hex(int(number))

def convertToBinary(number):
    return bin(int(number))

def isDec(number):
    if (number.isdigit()):
        return True
    else:
        return False

def isBin(number):
    try:
        int(number, 2)
    except ValueError:
        return False
    return True

def isHex(number):
    if (not isDec(number)) and (not isBin(number)):
        try:
            int(number, 16)
            return True
        except ValueError:
            return False
    else:
        return False


def checkDecimalType(number):
    if isDec(number):
        print(number)
    if isHex(number):
        print(convertToDecimal(number, 16))
    if isBin(number):
        print(convertToDecimal(number, 2))

def checkHexadecimalType(number):
    if isDec(number):
        print(convertToHexaDecimal(number))
    if isHex(number):
        print(number)
    if isBin(number):
        print(convertToHexaDecimal(convertToDecimal(number, 2)))

def checkBinaryType(number):
    if isDec(number):
        print(convertToBinary(number))
    if isHex(number):
        print(convertToBinary(convertToDecimal(number, 16)))
    if isBin(number):
        print(number)

number = input("Please Input a Number in Dec, Bin or Hex Format: ")
output = int(input("1: Decimal\n2: Hexadecimal\n3: Binary "))

if output == 1: # Decimal
    checkDecimalType(number)

if output == 2: # Hexadecimal
    checkHexadecimalType(number)

if output == 3: # Binary
    checkBinaryType(number)        

# 23 0b10111, 0x17

