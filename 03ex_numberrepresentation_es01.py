def convert_2_bin(to_bin):
    print("Binary Converter")
    bin_to_bin = bin(to_bin)
    print("Value in Binary:",bin_to_bin)

def convert_2_dec(num):
    print("Decimal Converter")
    bin_num = int(num)
    print("Value in Decimal:",bin_num)
    
def convert_2_hex(to_hex):
    print("Hex Converter")
    to_hex = hex(to_hex)
    print("Value in Hexadecimal:",to_hex)
 
to_bin= 0x8d
convert_2_bin(to_bin)
to_bin=152
convert_2_bin(to_bin)

num=0x8d
convert_2_dec(num)
num= 0b10011000
convert_2_dec(num)

to_hex=152
convert_2_hex(to_hex)
to_hex = 0b10001101
convert_2_hex(to_hex)