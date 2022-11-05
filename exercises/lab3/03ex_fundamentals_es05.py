# Quadratic solution

import math
import cmath

a = 0.001
b = 1000
c = 0.001

print("\nExercise 5a)")

def quadSol1(a,b,c): # function for the equation ax^2 + bx + c = 0
    delta_sqrt = math.sqrt((b**2)-(4*a*c))
    if delta_sqrt < 0:
        print("There are no solution (the solutions are complex)")
        return
    x1 = (- b + delta_sqrt) / (2 * a)
    x2 = (- b - delta_sqrt) / (2 * a)
    return x1, x2

sola1,sola2 = quadSol1(a,b,c)
print("Solution a1: "+str(sola1))
print("Solution a2: "+str(sola2))

print("\nExercise 5b)")

def quadSol2(a,b,c):
    delta_sqrt = math.sqrt((b**2)-(4*a*c))
    if delta_sqrt < 0:
        print("Can not resolve the quadratic equation because the solutions are complex")
        return
    x1 = ((- b + delta_sqrt)*(- b - delta_sqrt)) / ((2 * a)*(- b - delta_sqrt))
    x2 = ((- b - delta_sqrt)*(- b + delta_sqrt)) / ((2 * a)*(- b + delta_sqrt))
    return x1, x2

solb1,solb2 = quadSol2(a,b,c)
print("Solution b1: "+str(solb1))
print("Solution b2: "+str(solb2))

# Every time multiplication (or division) is performed in the result an approximation is introduced into the result.
# Consequently, the results of (a) and (b) are a little different.

print("\nExercise 5c)")

def quadSol3(a,b,c):
    delta_sqrt = cmath.sqrt((b**2)-(4*a*c))
    x1 = (- b + delta_sqrt) / (2 * a)
    x2 = (- b - delta_sqrt) / (2 * a)
    return x1, x2

solc1,solc2 = quadSol3(6,1,5)
print("Solution c1: "+str(solc1))
print("Solution c2: "+str(solc2))