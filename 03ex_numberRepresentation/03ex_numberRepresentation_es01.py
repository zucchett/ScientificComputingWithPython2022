a = int(input("Enter a decimal number: "))

print(type(a))
a_bin = bin(a)
print('Binary representation of', a, ':', a_bin)

a_hex = hex(a)
print('Hexadecimal representation of', a, ':', a_hex)

print("")


print("Enter a binary number: ", end="")
b = input()
print(type(b))

b1 = int(b, 2)
b_hex = hex(b1)
print("Hexadecimal representation of",b, ":" ,b_hex)


b_dec = int(b, 2)
print("Decimal representation of", b, ":" ,b_dec)


print("")

print("Enter a hexadecimal number: ", end="")
c = input()
print(type(c))

c_dec = int(c, 16)
print("Decimal representation of", c, ":" ,c_dec)

c_bin = bin(c_dec)

print("Binary representation of", c, ":" ,c_bin)

