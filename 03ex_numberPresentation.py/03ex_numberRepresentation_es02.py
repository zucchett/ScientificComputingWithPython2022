# 2. 32-bit floating point number

binary_string = "110000101011000000000000"


def Convert(x):
    if x[0] == "1":
        sign = -1
    else:
        sign = 1
    exp_bin = ""

    for i in range(1, 9):
        exp_bin = exp_bin + x[i]
    m_bin = ""

    for i in range(9, 31):
        m_bin = m_bin + x[i]
    exp = int(exp_bin, 2)
    mantissa = 1

    counter = 1
    for i in m_bin:
        mantissa = mantissa + (int(i) / 2 ** counter)
        counter = counter + 1
    mantissa = mantissa * sign

    print("Sign: " + str(sign))
    print("Exponent: " + str(exp))
    print("Mantissa: " + str(mantissa))
    return mantissa * (2 ** (exp - 127))


print("Result: ", Convert("00000011111000000000000000000000"))
