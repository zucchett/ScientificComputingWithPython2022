"""
6\. **Nested functions**

Write two functions: one that returns the square of a number, and one that returns its cube.

Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.
"""


def square(X):
    return X * X


def cube(X):
    return X * X * X


def sixth_power(X):
    return square(X) * cube(X) * int(cube(X) / square(X))
    # return square(x)*cube(x)*x


x = 4
print("Result of function: " + str(sixth_power(x)))
print("Result of calculation: " + str(x ** 6))
