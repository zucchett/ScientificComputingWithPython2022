# Machine precision

def findPrecision(init_n, precision):
    while (init_n + precision != init_n):
        precision = precision/2
    return precision

print(findPrecision(1,0.1))