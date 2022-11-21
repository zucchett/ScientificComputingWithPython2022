#Number representation

# a binary or hexadecimal number should be entered as strings

def convert_type(x, output_type):
    s = str(x) + ' '
    if s[1] == 'b' : 
        y = int(x,2)
        return output_type(y)
    if s[1] == 'x' : 
        y = int(x,16)
        return output_type(y)
    else :
        return output_type(y)
    
print(convert_type('0x17',int))