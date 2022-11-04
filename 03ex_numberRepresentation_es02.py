N="11000000101100000000000000000000"
def floating_point(n):
    
    num = list (map(int, str(n)))    
    sign = (-1) ** num[0]
    exp = 0
    
    for ii in range(1, 9):
        exp += num[ii] * pow(2, (8-ii))
    
    exp -= 127   
    mantissa = 1
    
    for ii in range(1, 24):
        mantissa += num[ii+8] * pow(2, (-ii))
    
    return sign * mantissa * pow(2, exp)
    
    
print('11000000101100000000000000000000 corresponding floating point is: ', floating_point(N))
