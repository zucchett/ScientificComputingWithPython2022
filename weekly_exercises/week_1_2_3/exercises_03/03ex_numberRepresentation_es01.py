#Zuccolo Giada, matr. 2055702
# EXE 1

def determineInput():
    type_in = ""
    print(">>>> SET INPUT VALUE")
    foundB, foundD, foundH, foundType = False, False, False, False
    while not foundType:
        input_data = (input("Enter the number: ")).upper()
        if (set(input_data) | {'0', '1'}) == {'0', '1'}:
            foundB = True
            type_in = "BIN"
            foundType = True
        if (set(input_data)
                | {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}) == {
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
                }:
            foundD = True
            foundType = True
            type_in = "DEC"
        if (set(input_data)
                | {
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
                    'D', 'E', 'F'
                }) == {
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
                    'D', 'E', 'F'
                }:
            foundH = True
            foundType = True
            type_in = "HEX"
        if not foundType:
            print("[ERROR]: You insert a wrong input, try again")
        else:
            if (foundB and foundH and foundD):
                confirm_type = int(input(
                    "Which type of number is it? \n1- HEX\n2- DEC\n3- BIN\nChoose: "))
                if (confirm_type == 1):
                    type_in = "HEX"
                if (confirm_type == 2):
                    type_in = "DEC"
                if (confirm_type == 3):
                    type_in = "BIN"
            elif (foundH and foundD):
                confirm_type = int(input(
                    "Which type of number is it? \n1- HEX\n2- DEC\nChoose: "))
                if (confirm_type == 1):
                    type_in = "HEX"
                if (confirm_type == 2):
                    type_in = "DEC"
            return input_data, type_in


def determineTypeOut(type_input):
    print("\n>>>> SET OUTPUT VALUE")
    repres = ["BIN", "DEC", "HEX"]
    repres.remove(type_input)
    goodOut = False
    while not goodOut:
        select = int(input("In which representation do you want to convert? \n1- "+repres[0]+"\n2- "+repres[1]+"\nChoose: "))
        if select != 1 and select != 2:
            print("[ERROR]: You insert a wrong number, try again")
        else:
            if select == 1:
                return repres[0]
            if select == 2:
                return repres[1]

def conversion(inputs, type_out):
    print("\n>>>> CONVERSION:")
    if inputs[1] == "BIN" and type_out == "DEC":
        return int(inputs[0], 2)
    if inputs[1] == "BIN" and type_out == "HEX":
        return ((hex(int(inputs[0], 2))).upper()).replace("0X","")

    if inputs[1] == "DEC" and type_out == "BIN":
        return bin(int(inputs[0])).replace("0b", "")
    if inputs[1] == "DEC" and type_out == "HEX":
        return hex(int(inputs[0])).replace("0x", "").upper()

    if inputs[1] == "HEX" and type_out == "DEC":
        return int(inputs[0], 16)
    if inputs[1] == "HEX" and type_out == "BIN":
        return bin(int(inputs[0], 16)).replace("0b", "")



input_values = determineInput()

type_output = determineTypeOut(input_values[1])

output_value = conversion(input_values, type_output)
print("("+input_values[1] + ") \t " + input_values[0] +"\t-> "+ str(output_value)+"\t ("+type_output+")")
