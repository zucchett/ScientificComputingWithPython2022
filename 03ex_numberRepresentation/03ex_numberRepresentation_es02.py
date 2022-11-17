#32-bit floating point number

# x is a 32 bit binary string
# i used the function of the previous exercice 

def convert_type(x, output_type):
    s = str(x) + ' '
    if s[1] == 'b' : 
        y = int(x,2)
        return output_type(y)
    if s[1] == 'x' : 
        y = int(x,16)
        return output_type(y)
    else :
        return output_type(y)


def float_point_number(x):
    exponent = '0b'+ x[1:9]
    exponent = convert_type(exponent,int) - 127
    mantissa = 0
    y = x[9:]
    for i in range(1,24):
        mantissa += int(y[i-1])*2**(-i)
    return ((-1)**(int(x[0]))*(1+mantissa)*2**exponent)

print(float_point_number('01000011010101000000000000000000'))   