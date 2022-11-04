# 1. Number representation


def ConvertNumber(number: int, type_number: str):
    bin_number = bin(number)
    hex_number = hex(number)

    if type_number == "bin":
        return bin_number
    elif type_number == "hex":
        return hex_number
    return number


number = int(input("Enter a number: "))
print("Decimal representation: " + str(ConvertNumber(number, "dec")))
print("Binary representation: " + str(ConvertNumber(number, "bin")))
print("Hexadecimal representation: " + str(ConvertNumber(number, "hex")))
