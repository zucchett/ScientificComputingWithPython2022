#Zuccolo Giada, matr. 2055702
# EXE 02
def setLen(bin):
    diff = 32-len(bin)
    add_str = ""
    for i in range(diff):
        add_str += "0"
    new_bin_value = add_str+bin
    return new_bin_value

# professor value
bin = "110000101011000000000000"
binary_num = setLen(bin)

def convertSPFPinDec(binary_num):
    #calculate exponent part
    exponent = int(binary_num[1:9], 2)

    #calculate fractional part
    fraction = binary_num[9:32]
    def fractionPart(fraction):
        mantissa = 0
        pos = 1
        for i in fraction:
            if i == "1":
                mantissa += 2**(-pos)
            pos += 1
        return mantissa

    #calculate sign
    def sign_bit(x, num):
        if x==0:
            return num
        else:
            return -num
    new_value = sign_bit(binary_num[:1], (1 + fractionPart(fraction)) * 2**(exponent-127))
    return new_value


print("Binary num: \t\t\t" + binary_num)
print("Decimal representation: \t" + str(convertSPFPinDec(binary_num)))