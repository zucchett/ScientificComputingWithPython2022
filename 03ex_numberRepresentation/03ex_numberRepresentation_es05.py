# ex_05: quadratic solution

import math

def quadratic(p, q, r):
    x1 = (-1*q + math.sqrt(q**2 -4*p*r)) / (2*p) 
    x2 = (-1*q - math.sqrt(q**2 -4*p*r)) / (2*p)
    return x1, x2

def alternative_solution(x, y, z):
    x3 = (-1*y + math.sqrt(y**2 -4*x*z)) * (-1*y - math.sqrt(y**2 -4*x*z))/ (2*x * (-1*y - math.sqrt(y**2 -4*x*z)))
    x4 = (-1*y - math.sqrt(y**2 -4*x*z)) * (-1*y + math.sqrt(y**2 -4*x*z))/ (2*x * (-1*y + math.sqrt(y**2 -4*x*z)))
    return x3, x4

def mySolution(x, y, z):
    x5 = 4*x*z/ (2*x * (-1*y - math.sqrt(y**2 -4*x*z)))
    x6 = (-1*y - math.sqrt(y**2 -4*x*z)) / (2*x)
    return x5, x6

a = 0.001
b = 20
c = 0.0001

print("The solution using the standard formula is: \n", quadratic(a,b,c))
print("The solution using the second method is: \n", alternative_solution(a,b,c))
print()

print("The correct solution is: ", mySolution(a,b,c))

# Using the quadratic() the result obtained for the positive solution is incorrect because we are subtracting two very closed numbers
# Using the alternative_solution()the result obtain is incorrect in all cases because we are subtracting very closed numbers
# Using the mySolution() the subtraction is avoided

