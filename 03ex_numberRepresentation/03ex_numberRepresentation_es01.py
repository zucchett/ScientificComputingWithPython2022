def convertor(stringA,stringB):
    t = stringA
#If the input is hex
    if t[0]=='0' and t[1]=='x':
        print("The input is a hex:", stringA)
        i = int(stringA, 16)
        if stringB == 'int':           
            print("The output is an integer: ",i)
        elif stringB == 'bin':
            j = bin(i)
            print("The output is a binary:",j)
#If the input is binary
    elif t[0] =='0' and t[1] =='b':
        print("The input is a binary:", stringA)
        i = int(stringA,2)
        if stringB == 'int':           
            print("The output is an integer: ",i)
        elif stringB == 'hex':
            j = hex(i)
            print("The output is a hex:",j)
#If the input is a decimal
    else:
        print("The input is a decimal:", stringA)
        i = int(stringA)
        if stringB == 'bin':
            j= bin(i)
            print("The output is a binary: ",j)
        elif stringB == 'hex':
            j = hex(i)
            print("The output is a hex:",j)
    
#testing the function
convertor("123","bin")
convertor("0b11000101","hex")
convertor("0xABCD","int")
