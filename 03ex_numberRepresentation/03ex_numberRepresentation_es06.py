from sympy import *
a = .00000001
x = Symbol('x')
y = x * (x - 1)
print("The "y.diff(x).evalf(subs={x:1}))
y1 = y.evalf(subs={x : (1 + a)})
y2 = y.evalf(subs={x : 1})
y_prime = (y1 - y2) / a
print(y_prime)


