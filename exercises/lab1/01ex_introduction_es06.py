# Casting

var1 = input("Variable 1: ")
var2 = input("Variable 2: ")
try:
    result = float(var1) + float(var2)
    print("Result of the operation (float): " + str(result))
    print("Result of the operation (integer): " + str(int(result)))
except:
        print("The operation variable 1 + variable 2 can not be performed")