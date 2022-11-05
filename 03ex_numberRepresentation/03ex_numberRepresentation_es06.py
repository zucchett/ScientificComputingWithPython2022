# pip install sympy
from sympy import *

def lim(expr):
    x = symbols('x')
    limitExpression = limit(expr, x, 0) 
    print('\u2202 /', '\u2202{} ='.format(chr(0x2093)), "{}".format(limitExpression),  "\n-------------------------")

def f(x):
    return x * (x + 1)

def derivative(x, h):
    return (f(x + h) - f(x)) / h

print("h: Power(-2)")
lim(derivative(1, 10 ** -2))
print("h: Power(-4)")
lim(derivative(1, 10 ** -4))
print("h: Power(-6)")
lim(derivative(1, 10 ** -6))
print("h: Power(-8)")
lim(derivative(1, 10 ** -8))
print("h: Power(-10)")
lim(derivative(1, 10 ** -10))
print("h: Power(-12)")
lim(derivative(1, 10 ** -12))
print("h: Power(-14)")
lim(derivative(1, 10 ** -14))