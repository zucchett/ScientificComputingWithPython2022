# 6. Nested Functions

def square(n):
    return n**2

def cube(n):
    return n**3

def power6(n, transform):
    return square(transform(n))


print(power6(3,cube))