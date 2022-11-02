# Defining types here for type safety
hexType = "hex"
binType = "bin"
decType = "dec"


def convert_numbers(number, typeToConvert):
    numberType = decType
    if type(number) == str:
        if number[1] == "b":
            numberType = binType
        elif number[1] == "x":
            numberType = hexType
        else:
            return "The input number is not int/bin/hex !!!"

    if typeToConvert == binType:
        if numberType == decType:
            return bin(number)
        elif numberType == hexType:
            return bin(int(number, 16))
        return number
    elif typeToConvert == hexType:
        if numberType == decType:
            return hex(number)
        elif numberType == binType:
            return hex(int(number, 2))
        return number
    else:
        if numberType == hexType:
            return int(number, 16)
        elif numberType == binType:
            return int(number, 2)
        return number


testNumber = 255
print("Dec to Hex of %d is: " % testNumber, convert_numbers(testNumber, hexType))
print("Dec to Bin of %d is: " % testNumber, convert_numbers(testNumber, binType))
print("Hex to Bin of %s is: " % hex(testNumber), convert_numbers(hex(testNumber), binType))
print("Hex to Dec of %s is: " % hex(testNumber), convert_numbers(hex(testNumber), decType))
print("Bin to Dec of %s is: " % bin(testNumber), convert_numbers(bin(testNumber), decType))
print("Bin to Hex of %s is: " % bin(testNumber), convert_numbers(bin(testNumber), hexType))
print("Also testing Dec to Dec of %s: " % testNumber, convert_numbers(testNumber, decType))
print("Also testing Hex to Hex of %s: " % hex(testNumber), convert_numbers(hex(testNumber), hexType))
print("Also testing Bin to Bin of %s: " % bin(testNumber), convert_numbers(bin(testNumber), binType))
