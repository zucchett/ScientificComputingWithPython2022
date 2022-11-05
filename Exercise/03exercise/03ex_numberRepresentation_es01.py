# 1. Number representation:
def convert(n):
    typeN = n[:2]
    match typeN:
        case "0x":
            print("Input type is Hexadecimal")
            n_dec = int(n,16)
            n_bin = bin(n_dec)
            n_hex = hex(n_dec)
        case "0b":
            print("Input type is Binary")
            n_dec = int(n,2)
            n_bin = bin(n_dec)
            n_hex = hex(n_dec)
        case _:
            print("Input type is Decimal")
            n_dec = int(n)
            n_bin = bin(n_dec)
            n_hex = hex(n_dec)

    # Ask user about the output format
    print("h. Hexadecimal ")
    print("b. Binary")
    print("d. Decimal")
    print("Enter your choice :- ")
    choice = input()
    if choice == 'h':
        print("Hexadecimal output is: " ,n_hex)
    elif choice == 'b':
        print("Binary output is: " ,n_bin)
    else:
        print("Decimal output is: " ,n_dec)
 
number= input("Enter your desired number")
convert(number)