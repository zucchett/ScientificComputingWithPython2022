"""6. Nested functions
Write two functions: one that returns the square of a number, and one that returns its cube.
Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.
"""


def num_square(n):
    square = n ** 2
    return square


def num_cube(n):
    cube = n ** 3
    return cube


def power_num(n):
    power = num_cube(num_square(n))
    return power


print(power_num(2))
