def ieee745(N):
    a = int(N[0])       
    print("sign, 1 bit: " , a)
    b = int(N[1:9],2)  
    print("exponent, 8 bits: ", b)
    c = int("1"+N[9:], 2)#
    print("fraction, len(N)-9 bits: ", c)

    return (-1)**a * c /( 1<<( len(N)-9 - (b-127) ))

N = "110000101011000000000000"  
print("IEEE 745 is: ", ieee745(N)  )  