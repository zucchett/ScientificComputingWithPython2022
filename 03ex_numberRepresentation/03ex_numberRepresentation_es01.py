x = input("Enter a value:").lower()
y = input("Enter the type you want your value to convert.Is it 'dec','bin' or 'hex'? :").lower()


# I WROTE FUNCTION WITHOUT RETURN STATEMENT BECAUSE I DO NOT NEED THEM AFTER FUNCTION
def converter(value, wanted_type):    
    if value.isdecimal() == True:      #If number is decimal number
        if wanted_type == "dec":
            print(f"The number was already decimal {value}")
            value = int(value)
        elif wanted_type == "bin":
            bin_value = bin(int(value))
            print(f"The number converted from decimal {value} to {bin_value}")
        elif wanted_type == "hex":
            hex_value = hex(int(value))
            print(f"The number converted from decimal {value} to {hex_value}")

    else:
        try:
            dec_value = int(value,2)  #Firstly try if the input is binary
            
            if wanted_type == "bin":
                print(f"The number was already binary {value}")
            elif wanted_type == "dec":
                print(f"The number converted from binary {value} to dec: {dec_value}")
            elif wanted_type == "hex":
                hex_value = hex(dec_value)
                print(f"The number converted from binary {value} to hex: {hex_value}")
        
        except ValueError:  #If the input is hexadecimal
            if wanted_type == "hex":
                print(f"The number was already hex {value}")
            elif wanted_type == "dec":
                dec_value = int(value, 16)
                print(f"The number converted from hex {value} to dec: {dec_value}")
            elif wanted_type == "bin":
                dec_value = int(value, 16)
                bin_value = bin(dec_value)
                print(f"The number converted from hex {value} to bin: {bin_value}")

                
converter(x, y) # Write the value you want to convert to the x are and type for y area such as ("dec","bin","hex")