# Number representation

def detInputType(num,n_type):
    if len(num) == 1: num = str(num).zfill(2)
    if num[1]=="x":
        print("The input is an Hexadecimal number")
        num = int(num,16)
    elif num[1]=="b":
        print("The input is a Binary number")
        num = int(num,2)
    else:
        num = int(num)
        print("The input is a Decimal number")

    if (n_type == 1):
        return bin(num)
    elif (n_type == 2):
        return num
    elif (n_type == 3):
        return hex(num)

try:        
    x_num = (input("Insert a number: \n"))
    x_type = int(input("Convertion: select 1 for binary, 2 for decimal, 3 for hexadecimal \n"))

    print(detInputType(x_num,x_type))
except:
    print("\nERROR: the input must be a binary, decimal or hexadecimal number")