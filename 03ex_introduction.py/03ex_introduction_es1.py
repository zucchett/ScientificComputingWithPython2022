user_number = input(' insert the value : ')
try :
    print(f'the binary type of inserted number is {bin(int(user_number))} and the decimal type is {hex(int(user_number))}')
except :
    if user_number[1] == 'x' :
        print(f'the binary type of inserted number is {bin(int(user_number,16))} and the decimal type is {int(user_number,16)}')
    elif user_number[1] == 'b' :
        print(f'the hexadecimal type of inserted number is {hex(int(user_number,2))} and the decimal type is {int(user_number,2)}')   

