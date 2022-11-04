#Zuccolo Giada, matr. 2055702
# EXE 7
from sympy import *
import math

def calculateIntegral(k, h, N):
    # k is the starting value of the sum
    value_sum = 0
    while k <= 100:
        # I calculate the extended Riemann definition of the integral
        value_sum = value_sum + (h * sqrt(1 - ((-1 + (h * k))**2)))
        k+=1
    lim = limit(value_sum, N, oo)
    return lim

print("Compute the integral")
print("expected value \t\t= ", (math.pi / 2))
N = 100
h = 2/N
rd = calculateIntegral(1, h, N)
print("Riemann definition \t= ", rd)

# print("\nDiffence = ", (math.pi / 2)-rd)
# difference = 0.00166207124564610
# the result is not the same but the difference is not so significantly