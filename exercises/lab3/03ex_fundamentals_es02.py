# 32-bit floating point number

def floatPointNum(bin_str):
    sign_bin = int(bin_str[0]) # sign
    exp_bin = int(bin_str[1:9],2) # exponent
    mant_bin = int("1"+bin_str[9:], 2) # fraction

    return (-1)**sign_bin * mant_bin /( 1<<( len(bin_str)-9 - (exp_bin-127) ))

bin_str = "110000101011000000000000"
bin_str = bin_str.zfill(32)
print(floatPointNum(bin_str))