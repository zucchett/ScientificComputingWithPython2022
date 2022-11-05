#1. Number representation


def Conv(x,Type): #x tejem tkoun 5   0x5grt  0b10101
    """Conv converts a given number to a desired representation"""
    y=str(x)+str(x)
    #Determine the type of the input
    if y[1]=="x":
        print("x is represented in the hexadecimal base")
    elif y[1]=="b":
        print("x is represented in the hexadecimal base")
    else:
        print("x is represented in the decimal base")

    #Convert the input into the desired representation 
    if Type=="hex":
        return hex(x)
    if Type=="bin":
        return bin(x)
    if Type=="decimal" and y[1]=="b":
        return int(x,2)
    else:
        return int(x,16)

x="0b111000"
y=Conv(x,"decimal")
print(y)
    

