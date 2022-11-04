def convertToInt(mantis):
    p = -1
    mantiss = 0
    for i in mantis:
        mantiss += (int(i) * pow(2, p))
        p -= 1
    return (mantiss + 1)

num = '110000101011000000000000'
sign_bit = int(num[0])
exponent_1 = int(num[1:9], 2)
exponent_2 = exponent_1 - 127
mantis = num[9:]

mantiss = convertToInt(mantis)

no = pow(-1, sign_bit) * mantiss * pow(2, exponent_2)

print(no)