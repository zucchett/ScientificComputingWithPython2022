# Machine precision

def findPrecision(init_n, precision):
    while (init_n + precision != init_n):
        precision = precision/10
    return precision

base = 1.0
accuracy = 0.1

print("the machine precision for floating point numbers is: "+str(findPrecision(base,accuracy)))