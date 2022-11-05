ieee_bin = input("Please enter your input :")
def convert_bin(ieee_bin):
    if len(ieee_bin)!=32:
        print("ERROR: Not a 32 bit binary string")
        return None
    sign = int(ieee_bin[0], 2)
    exponent = int(ieee_bin[1:9], 2)

    fraction_str = ieee_bin[9:]
    fraction = 0
    n = 1
    for f in fraction_str:
        fraction += int(f) * 2**(-n)
        n += 1

    return (-1)**sign * (1+fraction) * 2**(exponent-127)

print(convert_bin(ieee_bin))
