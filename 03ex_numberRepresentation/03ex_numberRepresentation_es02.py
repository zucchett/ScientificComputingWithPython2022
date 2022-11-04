def convert_to_float(stringA):
#sign
    s = stringA[0]
    s1=int(s)
#8_bits
    f = stringA[1:9]
    f1 = int(f,2)
#23_bits
    e= stringA[9:]
    j=0
    for i in range(23):
        if(e[i]=='1'):
            j+=2**(-i-1)
    j= j+1

    x = ((-1)**s1) * j *( 2 **(f1-127))
    return float(x)

print(convert_to_float("00000011111000000000000000000000"))
print(convert_to_float("11000000101100000000000000000000"))
