"""
2. 32-bit floating point number

Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision
floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and
exponent, according to the IEEE 754 recommendations.
"""

a = "110000101011000000000000"


def tofloat(w):
    e = int(w[1:9], 2)
    rang = [i for i in range(1, 24)]
    f = list(map(lambda x: x[0] * 2 ** (-x[1]), list(zip([int(x) for x in w[9:32]], rang))))
    print("f: ", f)
    n = (-1) ** int(w[0]) * 2 ** (e - 127) * (sum(f) + 1)
    print("mantissa: ", sum(f) + 1)
    print("exponent: ", e - 127)
    print("sign: ", (-1) ** int(w[0]))
    return n


print("Computing over a:", a, "which correspond to -88 in floating point representation with 32 bits\n")
print("\n Result: ", tofloat(a))
