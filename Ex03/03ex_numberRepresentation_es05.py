#  5. Quadratic solution
import math


def quadraticRoots (a,b,c):
    x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
    print(x1,x2)

def reexpressQuadraticRoots (a,b,c):
    x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
    print(x1,x2)

quadraticRoots(0.001,1000,0.001)
reexpressQuadraticRoots(0.001,1000,0.001)