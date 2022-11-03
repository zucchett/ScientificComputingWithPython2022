#2. 32-bit floating point number


def conv_float(binary_string): #s="00000011111000000000000000000000"

    s=int(binary_string[0]) #1
    e=int("0b"+binary_string[1:9],2) #0b10000101 --> 1+4+2**7
    f=binary_string[9:] #011000000000000
    
    bias=127 #single precision

    #now let's calculate the fractional part in the decimal base
    f_=0
    for i in range(1,24):
        f_+=(2**(-i))* int(f[i-1])
    
    x_float=((-1)**s) * (1+f_) * 2**(e-bias)
    return x_float


binary_string="00000011111000000000000000000000"
print(conv_float(binary_string))
    
