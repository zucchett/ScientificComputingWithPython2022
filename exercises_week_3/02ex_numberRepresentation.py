#2. 32-bit floating point number

def floating_point(x):
    l = len(x) #should be 32
    
    s = None #sign
    exp = None #exponent
    m = 0 #mantissa

    #check of the sign
    s = int(x[0])
    print("Sign bit: "+str(s)) 
    exp_bits = x[1:9] #bits of the exponent
    print("Exponent bits: "+ exp_bits)
    m_bits = x[9:l] #bits of the mantissa minus the first bit
    print("Mantissa bits: "+m_bits)
    
    #evaluation of the exponent
    exp = 0
    l = len(exp_bits)
    for i in (range(l)):
        l -= 1       
        if(exp_bits[i] == "1"):          
            exp += 2**l    
    exp = 2**(exp-127)

    #evaluation of mantissa
    l = len(m_bits) 
    for i in (range(l)): 
        if(m_bits[i] == "1"):
            m += 2**(-(i+1))
    m = 1 + m    
    
    #evaluation of x
    x = ((-1)**s) * m * exp
        
    return x

print(floating_point('00000000110000101011000000000000'))