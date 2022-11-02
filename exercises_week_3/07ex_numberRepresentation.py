from cmath import sqrt
from sympy import *

N = 100
h = 2/N
s = 0

def f(x):
    return sqrt(1-x**2)

for x in range(2):
    s = s + h*f(3)
    
i = limit(s,N,oo)
print(i)