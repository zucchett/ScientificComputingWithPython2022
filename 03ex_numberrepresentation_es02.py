def spfp (n):
    sign = n[0]
    exponent = n[1:9]
    ment = n[9:]

    exp = int(exponent, 2) - 127
    r_bin = '1' + ment[:exp]
    f_bin = ment[exp:]

    r = int(r_bin, 2)
    f = 0
    for i in range(len(f_bin)):
        if (f_bin[i] == '1'):
            f += 2**(-i-1)

    result = r + f
    if (sign == '1'):
        result = -result

    return float(result)

num = '11000010101100110011000000110000'
print(f"\nThe coverted number is {spfp(num)} in decimal representation\n")