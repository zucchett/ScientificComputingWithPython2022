
def get_bit():
    while True:
        bit=()
        bit=input("Please enter 32 Bit binary number:")
        if (len(bit) != 32):
            continue
        y=1
        for i in range(len(bit)):
            if ((bit[i] != "0") and (bit[i] != "1")):
                y=0
                #print(y)
        if(y==0):
            continue
        elif (len(bit) == 32):
            return bit

def sign_bit(n):
    print(n)
    if (n[0]==1):
        sign=-1
    else:
        sign=1
    return sign

def exponent_of_bit(n):
    n.reverse()
    exponent=0
    for i in range(23,31):
        if (n[i]==1):
            exponent=2**(i-23)+exponent        
    return exponent

def mantissa_of_bit(n,x):
    n.reverse()
    mantissa=0
    for i in range(9,31):
        if (n[i]==1):
            mantissa=2**(-(i-8))+mantissa
    mantissa=(mantissa+1)*x       
    return mantissa
        
bit=get_bit()
bit=list(map(int, bit))
#bit="11000000101100000000000000000000"
#bit="00000011111000000000000000000000"
#bit="11000000111100000000000000000000"
sign=sign_bit(bit)
exponent=exponent_of_bit(bit)
mantissa=mantissa_of_bit(bit,sign)
result=mantissa*2**(exponent-127)
print(result)



