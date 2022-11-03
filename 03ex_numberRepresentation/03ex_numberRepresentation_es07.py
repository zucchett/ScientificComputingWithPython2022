from sympy import*
import math
import timeit

def calculate_dims(delta, x= -1.0):
    z = Symbol('z')
    y = 1 - (z**2)
    x_values=[x]
    while x < 1.0:
        x = x+(delta)
        x_values.append(x)
    y = [y.evalf(subs = {z: a}) for a in x_values]
    return y

def calculate_area(y,delta):
    a = sum([delta*b for b in y])
    print("Area for n = ", 2/delta, " is ",a)
    return a

n = 100
t = 0
while t < 1:
    y = calculate_dims(2/n)
    t = timeit.timeit(lambda: calculate_area(y, 2/n), number = 1)
    n = n*2
    print("This is n: ", n)
    print("This is t: ", t)
print('______________________________')
while t < 60:
    y = calculate_dims(2/n)
    t = timeit.timeit(lambda: calculate_area(y, 2/n), number = 1)
    n = n*2
    print("This is n: ", n)
    print("This is t: ", t)
