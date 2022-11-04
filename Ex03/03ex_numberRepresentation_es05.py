#  5. Quadratic solution
import math


#Part a
def quadraticRoots (a,b,c):
    x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
    print(x1,x2)

#Part b
def reexpressQuadraticRoots (a,b,c):
    x1 = 2*c/(-b - math.sqrt(b*b - 4*a*c)) # rationalizing and simplifying
    x2 = 2*c/(-b + math.sqrt(b*b - 4*a*c))
    print(x1,x2)

quadraticRoots(0.001,1000,0.001)
reexpressQuadraticRoots(0.001,1000,0.001)

'''
The function for part a and part b, return one correct and one incorrect root each.
For Part A: The second root is correct.
For Part B: The first root is correct.
The reason for this is that when we subtract two numbers very close to each other the algorithm becomes numerically unstable.
'''

#Part C

def stableQuadraticRoots (a,b,c):
    x1 = 2*c/(-b - math.sqrt(b*b - 4*a*c))
    x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
    print(x1,x2)

stableQuadraticRoots(0.001,1000,0.001)