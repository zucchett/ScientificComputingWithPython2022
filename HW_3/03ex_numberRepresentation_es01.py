# a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex)

def decimal_to_other(n):
    bin_conv = bin(n)
    print('decimal to Binary conversion', n, ':', bin_conv)
    hex_conv = hex(n)
    print('decimal to Hexadecimal conversion', n, ':', hex_conv)


def binary_to_other(n):
    # first convert binary to int
    num = int(n, 2)
    print("Binary to decimal conversion:", num)
    # then we convert int to hexadecimal
    hex_num = hex(num)
    return hex_num


def hexadecimal_to_other(n):
    hex_to_binary = bin(int(n, 16))
    print("hexadecimal to binary conversion :", hex_to_binary)
    hex_to_decimal = int(n, 16)
    return hex_to_decimal


decimal_to_other(34)
# Driver code
if __name__ == '__main__':
    print("binary to Hexadecimal conversion :", binary_to_other('0101001101'))
    print("Hexadecimal to decimal conversion :", hexadecimal_to_other('0F'))

