def square(x):
    return x**2

def cube(x):
    return x**3

def sixth(x):
    return square(cube(x))
print(f"The square of 5: {square(5)}")
print(f"The cube of 5: {cube(5)}")
print(f"The 6th power of 5: {sixth(5)}")
