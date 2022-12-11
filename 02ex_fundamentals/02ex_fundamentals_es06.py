def square(n):
    return n*n
def cube(n):
    return n*n*n
def sixth_power(n):
    return square(cube(n))

print(sixth_power(2))