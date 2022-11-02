from sympy import *

#function f(x) = x(x-1)
def f(x):
    return(x*(x-1))

#a
x = 1
delta = 10^(-2)
y = (f(x+delta)-f(x))/delta

l = limit(y,x,0,)
print(l)

#b
for i in range(4,15,2):
    delta = 10^(-i)
    y = (f(x+delta)-f(x))/delta
    l = limit(y,x,0)
    print(l)
#I HAVE NO CLUE 