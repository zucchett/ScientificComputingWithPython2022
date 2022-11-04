def changeRepresentation (number, outputType):
    if (number.startswith('0b')):
        try:
            n_bin = number
            n_dec = int(number, 2)
            n_hex = hex(n_dec)
        except:
            print("Apparantly input number is NOT a correct binary number!!! Check the input.")
            return
    elif (number.startswith('0x')):
        try:
            n_hex = number
            n_dec = int(number, 16)
            n_bin = bin(n_dec)
        except:
            print("Apparantly input number is NOT a correct hex number!!!  Check the input.")
            return
    else:
        if (not number.isdigit()):
            print("Number is NOT a correct integer number!!!")
            return
        n_dec = int(number)
        n_bin = bin(int(number))
        n_hex = hex(int(number))
        
    print("input number in",outputType,"would be :")    
    if (outputType == "d"):
        print(n_dec)
    if (outputType == "b"):
        print(n_bin)
    if (outputType == "h"):
        print(n_hex)

number = input ("Enter the number :")
outputType = input ("Enter output type ('d : dec', 'b : bin' or 'h : hex'):")
changeRepresentation(number, outputType)