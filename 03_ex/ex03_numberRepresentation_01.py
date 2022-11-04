dec_Type = "dec"# Defining types
hex_Type = "hex"# Defining types
bin_Type = "bin"# Defining types
def convert_function(number, type_c):#typeToConvert
    numberType = dec_Type
    if type(number) == str:
        if number[1] == "b":
            numberType = bin_Type
        elif number[1] == "x":
            numberType = hex_Type
        else:
            return "The input  is not correct !"

    if type_c == bin_Type:
        if numberType == dec_Type:
            return bin(number)
        elif numberType == hex_Type:
            return bin(int(number, 16))
        return number
    elif type_c == hex_Type:
        if numberType == dec_Type:
            return hex(number)
        elif numberType == bin_Type:
            return hex(int(number, 2))
        return number
    else:
        if numberType == hex_Type:
            return int(number, 16)
        elif numberType == bin_Type:
            return int(number, 2)
        return number


testNumber = 128
print("Dec to Hex of %d is: " % testNumber, convert_function(testNumber, hex_Type))
print("Dec to Bin of %d is: " % testNumber, convert_function(testNumber, bin_Type))
print("Hex to Bin of %s is: " % hex(testNumber), convert_function(hex(testNumber), bin_Type))
print("Hex to Dec of %s is: " % hex(testNumber), convert_function(hex(testNumber), dec_Type))
print("Bin to Dec of %s is: " % bin(testNumber), convert_function(bin(testNumber), dec_Type))
print("Bin to Hex of %s is: " % bin(testNumber), convert_function(bin(testNumber), hex_Type))


