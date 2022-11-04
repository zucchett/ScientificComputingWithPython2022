def BinaryChecker(x):
    try:
        val = int(x,2)
        return True
    except:
        return False

def HexadecimalChecker(x):
    try:
        val = int(x,16)
        return True
    except:
        return False
    
def NumberConvertion(inputValue,outputType):
    #Given that there is an input that is either bin/hex/dec
    #Given that there is a dedicated output type
    #Post => Turn the input into dedicated type and return
    
    if BinaryChecker(inputValue) == True: #number is binary
        if outputType == 'dec':
            return int(inputValue,2)
        elif outputType == 'hex':
            integer = int(inputValue,2)
            return hex(integer)
        else:
            return inputValue
    
    else: #number is decimal or hexadecimal
        if HexadecimalChecker(inputValue) == True: #number is hexadecimal
            if outputType == 'dec':
                return int(inputValue,16)
            elif outputType == 'hex':
                return inputValue
            else:
                integer = int(inputValue,16)
                return bin(integer)
        else: #number is decimal
            if outputType == 'dec':
                return inputValue
            elif outputType == 'hex':
                return hex(inputValue)
            else:
                return bin(inputValue)

s = input("Please enter a value:")
NumberConvertion(s, "hex") 