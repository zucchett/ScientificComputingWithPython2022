'''
function char_to_int takes a char as input and maps it to int:
'''
def char_to_int(ch):
    try: 
        return int(ch)
    except: 
        return int(ord(ch) - ord('a') + 10)

'''
function int_to_char takes an int value and maps it to char
'''
def int_to_char(i):
    if i>9: return chr(i + ord('a') - 10)
    return str(i)
'''
 this function takes an input string, reads it according to a base representation
  and finally returns the number
'''
def read_num(stri, base):
    number = 0
    stri_len = len(stri) - 1
    for i in range(0, stri_len +1):
        number += char_to_int(stri[i]) * (base**(stri_len-i))
    return number
'''
 this functions converters a number to the corresponding representation
 in a given base 
'''
def change_to_base_rep(number, base):
    string = ''
    while number:
        string = int_to_char(number%base) + string
        number = number//base
    return string
'''
conversion amongs bin, dec, hex
'''
def converter(s, format_n):
    
    s = s.replace(" ", "")  # removing all spaces in the sng
    s = s.lower()           # using only lowercased letters
    
    if s[0] == '-': 
        sign = -1
    else: 
        sign = 1
        
    s = s.replace("-", "")
    s = s.replace("+", "")
    
    if s.startswith('0b'): # the input sng represents a binary num
        if s[0] == '0':
            num = read_num(s[2:], 2)
        else:
            num = -1 * read_num(s[2:], 2)
    
    elif s.startswith('0x'): # the input sng represents a hex num
        if s[0] == '0':
            num = read_num(s[2:], 16)
        else:
            num = -1 * read_num(s[2:], 16)
    else:   
        num = read_num(s, 10)

        
            
    if format_n == 'dec':      
        result = change_to_base_rep(abs(num), 10)
    elif format_n == 'bin':    
        result = '0b' + change_to_base_rep(abs(num), 2)
    elif format_n == 'hex':    
        result = '0x' + change_to_base_rep(abs(num), 16)
    else:
        print('invalid format_n')
        return 0
    if sign == -1:
        return  '-' + result
    else:
        return result
    


print('0b111 to dec :', converter('-0b111','dec'))      # expected  7
print('124 to hex:', converter('124','hex'))            # expected  0x7c
print('0x7c to bin:', converter('0x7c','bin'))          # expected  0b1111100

