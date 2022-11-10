"""
1. Number representation

Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex).
Determine the input type in the function, and pass another argument to choose the output representation.
"""


def converter(a):
    string = str(a)

    if string[1] == "x":
        print("a is hex, converting to int and bin")
        return int(a, 16), bin(int(a, 16))
    elif string[1] == "b":
        print("a is bin, converting to int and hex")
        return int(a, 2), hex(int(a, 2))
    else:
        try:
            print("a is int, converting to bin and hex")
            return bin(a), hex(a)
        except:
            print("a is not either an int, bin or hex number")
    return


for a in ["0b1010", "10", "0xa", "test"]:
    for type_n in ["bin", "hex", "dec", "test"]:
        print("converting ", a, " into ", type_n)
        print(converter(a, type_n), "\n")
# a = 100  # Example
# a_hex = hex(a)
# b, c = converter(a_hex)
# print(b, c)
# print(type(b), type(c))
