# 1. Number representation

# Write a function that converts numbers among the bin, dec, and hex representations 
# (bin<->dec<->hex).
# Determine the input type in the function, and pass another argument to choose 
# the output representation.

def converter(number:int, type_number:str):
    number_bin = bin(number)
    number_hex = hex(number)
    if type_number == "bin":
        return number_bin
    elif type_number == "hex":
        return number_hex
    return number # default case

number = int(input("Enter an integer: "))
print("Decimal representation: "+str(converter(number, "dec")))
print("Binary representation: "+str(converter(number, "bin")))
print("Hexadecimal representation: "+str(converter(number, "hex")))