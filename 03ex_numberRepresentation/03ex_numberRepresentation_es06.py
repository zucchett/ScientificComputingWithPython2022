"""
6. The derivative
Write a program that implements the function f = x*(x-1)
a) Calculate the derivative of the function at the point x=1 using the derivative definition:
"""

from sympy import *
# a)-2
x = Symbol("x")
f = x * (x - 1)
df = diff(f, x)
df = lambdify(x, df)
print("Result of the function : ", df(1))


# a)-2
def f(x):
    return x * (x - 1)


def true_value(fx, vx):
    b = 1e-2  # 等于10的-2次方
    df = fx(vx + b) - fx(vx)
    dx = b
    result = df / dx
    return float("%f" % result)


print("Result of the function with b=0.01: ", true_value(f, 1))


# b)
def f(x):
    return x * (x - 1)


def other_value(fx, vx, b):
    df = fx(vx + b) - fx(vx)
    dx = b
    result = df / dx
    return float("%f" % result)


b = 1e-2
for i in range(0, 6):
    b = b * 1e-2
    print("Result of the function with b ", "%.14f" % b, ":", other_value(f, 1, b))
