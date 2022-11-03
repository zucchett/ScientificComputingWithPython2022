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

to_bin = 0x4f
convert_bin(to_bin)
to_bin = 90
convert_bin(to_bin)

num = 0x4f
convert_dec (num)
num = 0b10011
convert_dec(num)

to_hex= 0b10011
convert_hex(to_hex)
to_hex = 90
convert_hex(to_hex)






