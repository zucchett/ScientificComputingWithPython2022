from sympy import *
import math
x = Symbol('x')
f = x * (x - 1)
f_prime = diff(f, x)
print(f_prime)
f_prime = lambdify(x, f_prime)
print("Result of the derivative of the function: ", f_prime(1))

# a) 

def f(x):
    return x*(x-1)

def derivative1(function, value):
    h = 1e-2
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom

    return float("%f" % slope)
print("Result of the function with h equals to 0.01: ", derivative1(f, 1))

# b) T

def f(x):
    return x*(x-1)

def derivative2(function, value,h):
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom
    return float("%f" % slope)

h = 1e-2
for i in range(6):
    h = h * 1e-2
    print("Result of the function with h equals to","%.14f:" % h, derivative2(f, 1,h))
   