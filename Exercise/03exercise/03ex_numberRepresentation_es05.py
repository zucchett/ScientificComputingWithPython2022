#5. Quadratic solution
import math as m
#part a:
def findRoots(a,b,c):
    x1 = (-b + m.sqrt(b**2-(4*a*c))/(2*a))
    x2 = (-b - m.sqrt(b**2-(4*a*c))/(2*a))
    print("There are root1: ",x1, "& root2: ",x2)
    
findRoots(0.001,1000,0.001)

#part b:
def findRoots2(a,b,c):
    dev = 1/a
    x2 =  (-b + (b ** 2 - 4 * a * c) ** 0.5) * (0.5 * dev)
    x3 = (-b - (b ** 2 - 4 * a * c) ** 0.5) * (0.5 * dev)
    print("by re-expression formula there are root1: ",x2, "& root2: ",x3)
    #This answer is more accurate by re-expression the formula including: sqrt and division

findRoots2(0.001,1000,0.001)


#part c:
def findRoots3(a,b,c):
    r = b**2 - 4*a*c
    if r > 0:
        num_roots = 2
        x4 = (((-b) + m.sqrt(r))/(2*a))     
        x5= (((-b) - m.sqrt(r))/(2*a))
        print("There are 2 roots: %f and %f" % (x4, x5))
    elif r == 0:
        num_roots = 1
        x = (-b) / 2*a
        print("There is one root: ", x)
    else:
        num_roots = 0
        print("No roots, discriminant < 0.")

print("Apply a function for all cases")
findRoots3(0.001,1000,0.001)
    