#6. Nested functions
def square(x):
    return x**2

def cube(x):
    return x**3

def power():
    print(list(map(cube, map(square,range(3)))))
    
print("Power 6: ")
power()