def converter(n,type):
    if n[1] == 'b':
        if type=='bin':
            out = b
        if type=='dec':
            out = int(n,2)
        if type=='hex':
            out = hex(int(n,2))

    elif n[1] == 'x':
        if type=='bin':
            out = bin(int(n,16))
        if type=='dec':
            out = int(n,16)
        if type=='hex':
            out = n

    else:
        if type=='bin':
            out = bin(n)
        if type=='dec':
            out = n
        if type=='hex':
            out = hex(n)
    return out


a = input('Insert the number to be converted (i.e. 0xab, 0b101 or 135) and separated by a space the type needed as output (dec, hex or bin):')

x = a.split()
print(converter(x[0],x[1]))