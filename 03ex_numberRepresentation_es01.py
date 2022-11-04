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
def read_base_sng(stri, base):
    number = 0
    stri_len = len(stri) - 1
    for i in range(0, stri_len +1):
        # print(' reading', i, stri[i], char_to_int(stri[i]))
        number += char_to_int(stri[i]) * (base**(stri_len-i))
    return number
'''
 this functions converts a number to the corresponding string representation
 in a given base 
'''
def num_to_representation(number, base):
    string = ''
    while number:
        string = int_to_char(number%base) + string
        number = number//base
    return string
'''
conversion amongs bin, dec, hex
'''
def convert(s, target):
    s = s.replace(" ", "")  # removing all spaces in the sng
    s = s.lower()           # using only lowercased letters
    if s[0] == '-': sign_isnegative = True
    else: sign_isnegative = False
    s = s.replace("-", "");   s = s.replace("+", "");
    
    if s.startswith('0b'): # the input sng represents a binary num
        num = (1 if s[0] == '0' else -1) * read_base_sng(s[2:],2)
    elif s.startswith('0x'): # the input sng represents a hex num
        num = (1 if s[0] == '0' else -1) * read_base_sng(s[2:],16)
    else: # the input sng must be decimal
        num = read_base_sng(s,10)

    # print(' num in memory:', num)
    
    if target == 'dec':      out = num_to_representation(abs(num), 10)
    elif target == 'bin':    out = '0b' + num_to_representation(abs(num), 2)
    elif target == 'hex':    out = '0x' + num_to_representation(abs(num), 16)
    else:
        print('invalid target format')
        return 0
    
    return ('-' if sign_isnegative else '') + out
    
print('0b111 to dec :', convert('0b111','dec'))      # expected  7
print('124 to hex:', convert('124','hex'))        # expected  0x7c


