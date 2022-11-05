"""
1Number representation**
Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex).
Determine the input type in the function, and pass another argument to choose the output representation.

**数字表示法**
写一个函数，在bin二进制、dec十进制和hex十六进制表示法之间转换数字（bin<->dec<->hex）。
在函数中确定输入类型，并传递另一个参数来选择输出表示法。
"""
num = 10100
print(type(num))

def convert_num(num, opt):
    # 确认数据类型
    print(num,opt)
    type_num = type(num)
    print(type_num)
    if opt == "din_to_dec":
        din_dec = int(num, 2)  # 2-10
        print("Value in dec:", din_dec)
    elif opt == "bin_to_hex":
        bin_hex = hex(int(num, 2))  # 2-16
        print("Value in hex:", bin_hex)
    elif opt == "dec_to_hex":
        dec_hex = hex(num)[2:]  # 10-16
        print("Value in dec:", dec_hex)
    elif opt == "dec_to_bin":
        dec_bin = bin(num)[2:]  # 10-2 并进行切片操作
        print("Value in dec:", dec_bin)
    elif opt == "hex_to_dec":
        hex_bin = bin(int(num, 16))  # 16-2
        print("Value in dec:", hex_bin)
    elif opt == "hex_to_dec":
        hex_dec = int(num, 16)  # 16-10
        print("Value in dec:", hex_dec)
    return


input_num = input("write a number: ")
input_opt = input("write another argument to choose the output representation: ")

convert_num(input_num, input_opt)

