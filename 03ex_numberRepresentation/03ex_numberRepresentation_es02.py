b = '11001111100000011111000000000010'
def single_float(b):
    sign_value = (-1) ** int(b[0])
    exponent = int(b[1:9],2)
    mantis = sum([int(y)*(0.5**(x+1)) for x ,y in enumerate(b[9:])]) + 1
    if mantis == 1 and sign_value == 1 and exponent == 255:
        return (float("+inf"))
    elif mantis == 1 and sign_value == -1 and exponent == 255:
        return (float("-inf"))
    elif mantis > 1 and exponent == 255:
        return (float("nan"))
    else:
        return mantis * sign_value * (2**(exponent - 127))
print(single_float(b))

