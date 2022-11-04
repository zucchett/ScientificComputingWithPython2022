def binaryOfFraction(fraction):
    binary = str()
    while (fraction):
        fraction *= 2
        if (fraction >= 1):
            int_part = 1
            fraction -= 1
        else:
            int_part = 0
            
        binary += str(int_part)

    return binary

def floatingPoint(real_no):
    sign_bit = 0

    if(real_no < 0):
        sign_bit = 1


    real_no = abs(real_no)


    int_str = bin(int(real_no))[2 : ]

    fraction_str = binaryOfFraction(real_no - int(real_no))

    ind = int_str.index('1')

    exp_str = bin((len(int_str) - ind - 1) + 127)[2 : ]

    mant_str = int_str[ind + 1 : ] + fraction_str

    mant_str = mant_str + ('0' * (23 - len(mant_str)))

    return sign_bit, exp_str, mant_str


if __name__ == "__main__":

    sign_bit, exp_str, mant_str = floatingPoint(110000101011000000000000)

    ieee_32 = str(sign_bit) + '|' + exp_str + '|' + mant_str

    print("IEEE 754 representation of 110000101011000000000000 is :")
    print(ieee_32)

def convertToInt(mantissa_str):

    power_count = -1

    mantissa_int = 0

    for i in mantissa_str:

        mantissa_int += (int(i) * pow(2, power_count))

        power_count -= 1

    return (mantissa_int + 1)

if __name__ == "__main__":

    ieee_32 = '0|11001011|0111010010110001111000001111100001111111110111001110001010000011000000000000'

    sign_bit = int(ieee_32[0])

    exponent_bias = int(ieee_32[2 : 10], 2)

    exponent_unbias = exponent_bias - 127
    
    mantissa_str = ieee_32[11 : ]

    mantissa_int = convertToInt(mantissa_str)

    real_no = pow(-1, sign_bit) * mantissa_int * pow(2, exponent_unbias)

    print("The float value of the given IEEE-754 representation is :",real_no)
