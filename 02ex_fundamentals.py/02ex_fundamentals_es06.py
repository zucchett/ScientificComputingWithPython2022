# 6. Nested functions

# Write two functions: one that returns the square of a number,
# and one that returns its cube.
# Then, write a third function that returns the number raised to the 6th power,
# using only the two previous functions.
import math

def square(x):
    return math.pow(x,2)

def cube(x):
    return math.pow(x,3)

def sixth_pow(x):
    return square(cube(x))

print(sixth_pow(2))
