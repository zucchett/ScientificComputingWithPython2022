from sympy import *
# The accuracy has been increased by decreasing the delta until 1e-8. After that the accuracy decreased again because of the limitation in floating point
a = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
x = Symbol('x')
y = x * (x - 1)
def derivative(a):
    print("Compute derivative analytically: ",y.diff(x).evalf(subs={x: 1}))
    y1 = y.evalf(subs={x : (1 + a)})
    y2 = y.evalf(subs={x : 1})
    y_prime = (y1 - y2) / a
    print("Compute derivative by definition: ",y_prime)

for i in a:
    print("Derivative for delta = ", i)
    derivative(i)
    print("______________________")


