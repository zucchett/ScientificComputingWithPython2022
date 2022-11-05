def square(x):
    return x*x

def cube(x):
    return x*x*x

def powerSix(x):
    return cube(square(x))

print(powerSix(2))