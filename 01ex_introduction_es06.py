x1 = input("Enter type of your first input: ")
x2 = input("Enter type of your second input: ")

try:
    x1 = int(x1)
except:
    try:
        x1 = float(x1)
    except:
        pass

try:
    x2 = int(x2)
except:
    try:
        x2 = float(x2)
    except:
        pass

try:
    x3 = x1 + x2
    print("addition is possible  and result is :", x3,"\nx1 is defined as",type(x1),"and x2 is defined as",type(x2),)
except:
    print("addition is NOT possible for these two inputs.\n","x1 is defined as",type(x1),"and x2 is defined as",type(x2))