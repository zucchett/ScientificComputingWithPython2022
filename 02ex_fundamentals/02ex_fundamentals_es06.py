def cube (x):
    return x ** 3

def square (x):
    return x ** 2

def sixth_power(x):
    return(cube(square(x)))

print(sixth_power(2))
