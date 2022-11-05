def square(x):
    return x ** 2# returns the square of a number
def cube(x):
    return x ** 3# returns the cube of a number
def sixth_power(x):
    return square(cube(x)) # the 6th power
print(sixth_power(3))