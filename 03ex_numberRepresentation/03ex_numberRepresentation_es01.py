def n_conversion(n, ntype):
    
        if isinstance(n,str): 
            if n.startswith('0b'):
                itype = 'bin'
                n = int(n,2)
                
            elif n.startswith('0x'):
                itype = 'hex'
                n = int(n, 16)
               
        else:
            itype = 'dec'
        
        if itype != ntype:
            if ntype == 'dec':
                return n
            elif ntype == 'bin':
                return bin(n)
            else:
                return hex(n)
        else:
            return n
            

a = 0b011
b = 12
c = 0x34

print('Binary to Integer: ',bin(a), "to" ,n_conversion(a,'dec'))
print('Binary to Hexadecimal: ',bin(a), "to" ,n_conversion(a,'hex'))

print('Integer to Binary: ',b, "to" ,n_conversion(b,'bin'))
print('Integer to Hexadecimal: ',b, "to",n_conversion(b,'hex'))

print('Hexadecimal to Binary: ',hex(c), "to" ,n_conversion(c,'bin'))
print('Hexadecimal to Integer: ',hex(c), "to" ,n_conversion(c, 'dec'))
