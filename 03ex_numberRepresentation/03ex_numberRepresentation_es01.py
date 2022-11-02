# 1. Number representation

# Write a function that converts numbers among the bin, dec, and
# hex representations (bin<->dec<->hex). Determine the input type in
# the function, and pass another argument to choose the output representation.

# -------------------------------------- Code Begin-------------------------------------



def convert(x,opt_rep):
    
    assert opt_rep in ['bin','dec','hex']
    
    x = str(x)
    if x[0:2] == '0b':
        print('{} is a Binary number'.format(x))
        if opt_rep == 'dec':
            return int(x,2)
        elif opt_rep == 'hex':
            return hex(int(x,2))
        else:
            return x
    elif x[0:2] == '0x':
        print('{} is a Hexdecimal number'.format(x))
        if opt_rep == 'dec':
            return int(x,16)
        elif opt_rep == 'bin':
            return bin(int(x,16))
        else:
            return x
    else:
        print('{} is a Decimal number'.format(x))
        if opt_rep == 'hex':
            return hex(x)
        elif opt_rep == 'bin':
            return bin(x)
        else:
            return x
        
a = hex(65)
b = bin(53)
print('Binary representation of', a, ':', convert(a,'bin'),'\n \n')
print('Hexadecimal representation of', b, ':', convert(b,'hex'),'\n \n')
print('Decimal representation of', a, ':', convert(a,'dec'),'\n \n')
print('Decimal representation of', b, ':', convert(b,'dec'),'\n \n')
# -------------------------------------- Code End-------------------------------------
