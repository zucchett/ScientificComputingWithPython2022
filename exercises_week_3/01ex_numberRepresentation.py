#1. Number representation

def converter(n,x):
        try:
                if n[0] == "0" and n[1] == "x":
                        n = int(n,16)
                        print("Your number is a hexadecimal")
                elif n[0] == "0" and n[1] == "b":
                        n = int(n,2)
                        print("Your number is a binary")
                else:
                        n = int(n)
                        print("Your number is decimal")
                
                if(int(x) == 1):
                        n = int(n)
                elif(int(x) == 2):
                        n = hex(n)
                        #n = n[2:len(n)]
                elif(int(x) == 3):
                        n = bin(n)
                        n = n[2:len(n)]
                return(n)
        except:
                print("There was a problem.")
                


n = input("Enter a hexadecimal (0x...), decimal or binary number (0b...):")    
x = input("Do you want to convert it to a: \n 1. Decimal \n 2. Hexadecimal \n 3. Binary \n")
print(f"The result is: {converter(n,x)} ")