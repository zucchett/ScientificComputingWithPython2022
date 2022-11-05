def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def sixth_power(x):
    return square(cube(x))


print(sixth_power(2))
