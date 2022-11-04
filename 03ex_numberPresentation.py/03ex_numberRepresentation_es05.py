# 5. Quadratic solution

import math


#A
def quad_1(a, b, c):
    factor = math.sqrt(b * b - 4 * a * c)
    return (-b + factor) / (2 * a), (-b - factor) / (2 * a)


print("quadratic 1 roots:  =", quad_1(0.001, 1000, 0.001))


#B

def quad_2(a, b, c):
    factor = math.sqrt(b * b - 4 * a * c)
    return 2 * c / (-b - factor), 2 * c / (-b + factor)


print("quadratic 2 roots: =", quad_2(0.001, 1000, 0.001))


#C
def quad_3(a, b, c):
    factor = math.sqrt(b ** 2 - 4 * a * c)
    return 2 * c / (-b - factor), (-b - factor) / (2 * a)


print("quadratic 3 roots: =", quad_3(0.001, 1000, 0.001))
