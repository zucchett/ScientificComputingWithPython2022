# ex_01

def converter(a, output_type):
    if a.find("b") == 1:
        input_type = 'bin'
        if output_type == "bin":
            output_a = a
        elif output_type == "hex":
            output_a = hex(int(a,2))
        else:
            output_a = int(a, 2)
    elif a.find("x") == 1:
        input_type = 'hex'
        if output_type == "bin":
            output_a = bin(int(a, 16))
        elif output_type == "hex":
            output_a = a
        else:
            output_a = int(a, 16)
    else:
        input_type = 'dec'
        if output_type == "bin":
            output_a = bin(int(a))
        elif output_type == "hex":
            output_a = hex(int(a))
        else:
            output_a = int(a)
    return input_type, output_a


a_in = (input("Enter a number in the representation you prefer: "))
representation = input("Enter if the output is bin, dec or hex: ")

repres, a_out = converter(a_in, representation)

print("The entered number is in", repres, "representation; the output in", representation, "representation is:", a_out)
