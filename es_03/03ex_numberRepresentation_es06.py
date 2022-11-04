# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 20:38:17 2022

@author: Federico
"""

def f(x): 
    return x*(x-1)
def numder_f(x, d):
    return (f(x+d)-f(x))/d
print("derivative: analytic calculation. f'(x) = 2x-1\n"
      "f'(1) =", 1)    
for i in range(2,20,2):
    print("delta =", 10**(-i),"  ", "f'_num =",numder_f(1, 10**(-i)), "   ","accuracy =", (numder_f(1, 10**(-i))-1))
"""    
the analytic and numerical results do not agree: this is due to the fact that the analytic definition of derivative is built on the
the limit for delta-> 0, which is incompatible with the finite precision of float operations.
As one can see, the accuracy of the calculation has a maximum for delta = 1e-08, then decreases again.
this is due to the fact that the numerator is the difference of two numbers very close to each other (so close that the difference becomes 0 for delta = 1e-16)
moreover the denominator is a very small float. the combination of these issues in float calculations leads to this 
accuracy scaling
"""