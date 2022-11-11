x = int(input("please enter a number:"))

def square(x):
    s = x * x
    return s
print("square is : ",square(x))

def cube(x):
    c = x * x * x
    return c
print("cube is : ",cube(x))

def sixthpower():
    z_1 = square(x) ** 6
    z_2 = cube(x) ** 6
    return z_1,z_2

print("sixth power of the number is:",sixthpower())