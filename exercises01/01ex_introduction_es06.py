var1 = input("Variable 1: ")
var2 = input("Variable 2: ")
try:
    var1 = int(var1)
    print("Variable 1 is an integer")
except:
    try:
        var1 = float(var1)
        print("Variable 1 is a float")
    except:
        print("Variable 1 is not a number")

try:
    var2 = int(var2)
    print("Variable 2 is an integer")
except:
    try:
        var2 = float(var2)
        print("Variable 2 is a float")
    except:
        print("Variable 2 is not a number")

try:
    result = var1+var2
    print("Result of the operation: " + str(result))
except:
    print("The operation variable 1 + variable 2 can not be performed")