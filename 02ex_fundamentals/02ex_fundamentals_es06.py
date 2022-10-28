import math
def sqr(x):
    a = x**2
    return a
def cub(x):
    b = x**3
    return b
def sixth(x):
    c = cub(x)*sqr(x)*x
    return c
d = sixth(2)
print(d)

