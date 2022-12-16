def num_squared(x):
    return x ** 2

def num_cubed(x):
    return x ** 3

def six_power(x):
    return num_cubed(num_squared(x))

six_power(2)