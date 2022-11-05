def convert (n):
    sign = n[0]
    exponent = n[1:9]
    mentisa = n[9:32]

    e = int(exponent, 2) - 127    # bias must be substracted from int representation of the exponent part
    m = 0
    for i, k in enumerate(mentisa):
        if (k == '1'):
            m += 2**(-i-1)
   
    result = (1.0 + m) * 2**e
    
    
    if (sign == '1'):
        print("number is : -", 1+m , "* 2 ^" , e)
        return float(-result)
        
    print("number is :", 1+m , "* 2 ^" , e)
    return float(result)

n1 = '110000101011000000000000'
n2 = '11000010101100110011000000110000'
n3 = '00011111111000001010101001110000'
print(convert(n1))
print(convert(n2))
print(convert(n3))