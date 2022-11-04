# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:37:26 2022

@author: Ruben
"""

def f(x):
    return x*(x-1)

def der(f,delta):
    return (f(1+delta)-f(1))/delta

print(der(f,10**(-2)))
print("\n")

#The result differs from 1 (the actual value of the derivative calculated in 1). The derivative 
#coincides with the ratio inside der() only if d goes to zero. We are instead using d=10**2

for i in range(-4,-16,-2):
    d=10**i
    print("Using d=10**%d The derivative of f calculated at x=1 is %.12f" %(i, der(f,d)))
    print("ratio between the accuracy of the previous d is %.12f" %((1-der(f,d))/(1-der(f,d*10**2))))
    print("\n")

#Better accuracy obtained for d=10**-8