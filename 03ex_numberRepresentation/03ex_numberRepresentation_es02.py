from math import inf, nan

prova_ex1 = '00000011111000000000000000000000'
prova_ex2 = '11000000101100000000000000000000'

pigreco = '01000000010010010000111111011011'
plus_infinity = '01111111100000000000000000000000'
minus_infinity = '11111111100000000000000000000000'
not_a_number = '01111111100000000001111111111111'

def conv(bin):
    sign = bin[0]
    exp = bin[1:9]
    last = bin[9:]
    bias = 127
    
    f = []
    for x in range(len(last)):
        f.append(int(last[x])/pow(2,x+1))

    mantissa = 1 + sum(f)
    
    if sign=='0' and int(exp,2)==255 and sum(f)==0:
        return +inf
    elif sign=='1' and int(exp,2)==255 and sum(f)==0:
        return -inf
    elif int(exp,2)==255 and sum(f)>0:
        return nan
    else:
        return pow(-1,int(sign))*mantissa*pow(2,int(exp,2)-bias)



print('Converting pi: ',conv(pigreco))
print('Converting first example from lecture: ',conv(prova_ex1))
print('Converting second example from lecture: ',conv(prova_ex2))
print('Converting plus infinity: ',conv(plus_infinity))
print('Converting minus infinity: ',conv(minus_infinity))
print('Converting NaN: ',conv(not_a_number))