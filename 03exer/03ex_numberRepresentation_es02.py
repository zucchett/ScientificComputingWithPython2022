#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it

def conversion(mantissa_str):
 

    power_count = -1
 

    mantissa_float = 0
 

    for i in mantissa_str:
        mantissa_float += (int(i) * pow(2, power_count))
 

        power_count -= 1
         

    return (mantissa_float + 1)
 
if __name__ == "__main__":

    ieee_32 = ""
    for i in range(32):
        Element = input("Insert 1 or 0: ")
        if Element == '1' or Element == '0':
            ieee_32 += Element
        else:
            
            raise ValueError('ERROR: A bit cannot be different from 0 or 1')


    sign = int(ieee_32[0])

 

    exponent_bias = int(ieee_32[1 : 9], 2)

    exponent_nobias = exponent_bias - 127
 

    mantissa_str = ieee_32[9 : ]
    
 

    mantissa_float = conversion(mantissa_str)
    real_number = pow(-1, sign) * mantissa_float * pow(2, exponent_nobias)
 

    print("The float value of the given IEEE-754 representation is :",real_number)
