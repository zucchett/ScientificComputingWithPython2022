
from sympy import limit
from sympy import *



def lim(x , y):
    l =  (fx(x + y) - fx(x)) / y
    print(l)


def fx(x):
    return x*(x-1)

print("(a)")
lim(1 , (10**-2))


print("(b)")
v = [-4,-6,-8,-10,-12,-14]
for i in v:
    lim(1 , (10**i))