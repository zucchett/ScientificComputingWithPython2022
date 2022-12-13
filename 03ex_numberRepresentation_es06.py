from sympy import limit
from sympy import *

def limit(x , y):
    l =  (fx(x + y) - fx(x)) / y
    print(l)


def fx(x):
    return x*(x-1)

print("section a")
limit(1 , (10**-2))


print("section b")
v = [-4,-6,-8,-10,-12,-14]
for i in v:
    limit(1 , (10**i))