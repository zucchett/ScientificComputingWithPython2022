def convert_bin (to_bin):
    bin_to_bin = bin(to_bin)
    print("the value in binary is:" , bin_to_bin)
    print(type(bin_to_bin))
def convert_dec (num):
    bin_num = int(num)
    print("the value in decimal is :" , bin_num)
    print(type(bin_num))
def convert_hex (to_hex):
    to_hex = hex(to_hex)
    print("the value in hexadecimal is:", to_hex)
    print(type(to_hex))

to_bin = 0x3c
convert_bin(to_bin)
to_bin = 60
convert_bin(to_bin)

num = 0x3c
convert_dec (num)
num = 0b111001
convert_dec(num)

to_hex= 0b11011
convert_hex(to_hex)
to_hex = 60
convert_hex(to_hex)






