bin_string = '11000000101100000000000000000000'

def floatConverter(bin_input):
    sign = int(bin_input[0])    
    exponent = int(bin_input[1:9], 2)
    mantissa = (bin_input[9:31])
    f = 0
    for i in range(len(mantissa)):
        f = f + int(mantissa[i])/(2**(i+1))
    int_output = (-1)**sign * (1+f) * 2**(exponent-127) 
    return int_output

print("The single precision floating point in decimal representation is: ", floatConverter(bin_string))
