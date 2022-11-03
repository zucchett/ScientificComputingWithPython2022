# Nested functions
def square(n):
    return n * n


def cube(m):
    return m * m * m


def sixth(o):
    return square(o) * cube(o)


print(sixth(7))
