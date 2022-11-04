# 1. Number representation

# Write a function that converts numbers among the bin,
# dec, and hex representations (bin<->dec<->hex).
# Determine the input type in the function, and pass
# another argument to choose the output representation.

def conversions(n, out_type = "dec"):
    print("The input number is " + str(n))
    if isinstance(n, str): # n is either binary or hexadecimal, so it is a string

        if n[1] == 'b': # n is binary
            if out_type == "bin":
                print("We want to convert a binary to a binary number.")
                output = n
            elif out_type == "hex":
                print("We want to convert a binary to a hexadecimal number.")
                output = hex(int(n, 2))
            else: # convert to decimal
                print("We want to convert a binary to a decimal number.")
                output = int(n,2)

        else : # n[1] == 'x', so n is hexadecimal

            if out_type == "bin":
                print("We want to convert a hexadecimal to a binary number.")
                output = bin(int(n, 16))
            elif out_type == "hex":
                print("We want to convert a hexadecimal to a hexadecimal number.")
                output = n
            else: # convert to decimal
                print("We want to convert a hexadecimal to a decimal number.")
                output = int(n, 16)
    
    else: # n is an int
        if out_type == "bin":
            print("We want to convert a decimal to a binary number.")
            output = bin(n)
        elif out_type == "hex":
            print("We want to convert a decimal to a hexadecimal number.")
            output = hex(n)
        else: # convert to decimal
            print("We want to convert a decimal to a decimal number.")
            output = n

    print("The result of the conversion is: " + str(output))

N = 10
M = "0b10110"

conversions(N, "hex")

conversions(M, "dec")

# ex01 done!
