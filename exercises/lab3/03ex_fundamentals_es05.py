# Quadratic solution

import math

print("\nExercise 5a)")

def quadSol1(a,b,c):
    if((b**2)-(4*a*c)<0):
        print("Can not resolve the quadratic equation because the solutions are complex")
        return
    delta_sqrt = math.sqrt((b**2)-(4*a*c))
    x1 = (-b+delta_sqrt)/ (2*a)
    x2 = (-b-delta_sqrt)/ (2*a)
    return x1,x2


sola1,sola2 = quadSol1(0.001,1000,0.001)
print("Solution a1: "+str(sola1))
print("Solution a2: "+str(sola2))

print("\nExercise 5b)")

def quadSol2(a,b,c):
    if((b**2)-(4*a*c)<0):
        print("Can not resolve the quadratic equation because the solutions are complex")
        return
    delta_sqrt = math.sqrt((b**2)-(4*a*c))
    x1 = ((-b+delta_sqrt)*(-b-delta_sqrt)) / ((2*a)*(-b-delta_sqrt))
    x2 = ((-b-delta_sqrt)*(-b+delta_sqrt)) / ((2*a)*(-b+delta_sqrt))
    return x1,x2


solb1,solb2 = quadSol2(0.001,1000,0.001)
print("Solution b1: "+str(solb1))
print("Solution b2: "+str(solb2))

print("\nExercise 5c)")