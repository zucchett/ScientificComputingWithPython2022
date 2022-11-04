
def binary(x,y):
    y = int(y, 2)
    if (x == "dec"):
        answer = int(y)
        print(answer)
    elif(x == "hex"):
        answer = hex(y)
        print(answer)
    return answer

def decimal(x,y):
    if (x == "bin"):
        answer = bin(y)
        print(answer)
    elif(x == "hex"):
        answer = hex(y)
        print(answer)
    return answer

def heximal(x,y):
    y = int(y, 16)
    if (x == "dec"):
        ans = int(y)
        print(ans)
    elif(x == "bin"):
        ans = bin(y)
        print(ans)
    return ans




number=[]
number = input("Please enter the number as binary, hexadecimal, decimal (i.e. 0xab, 0b101 or 39):")
print(number)
to_transfer=str(input("Please enter the type of number which will convert as bin, dec, hex:"))

if(number[1] == "b"):
    binary(to_transfer,number)
elif(number[1] == "x"):
    heximal(to_transfer,number)
else:
    decimal(to_transfer,number)
