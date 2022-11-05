import math as m
import numpy as np

def sol1(a,b,c):
    x1 = (-b-m.sqrt(pow(b,2)-4*a*c))/(2*a)
    x2 = (-b+m.sqrt(pow(b,2)-4*a*c))/(2*a)
    return [x1,x2]

def sol2(a,b,c):
    x1 = (4*a*c)/(-2*a*b+2*a*m.sqrt(pow(b,2)-4*a*c))
    x2 = (4*a*c)/(-2*a*b-2*a*m.sqrt(pow(b,2)-4*a*c))
    return [x1,x2]

def corrSol(a,b,c):
    r = (b**2-4*a*c)**0.5
    x1 = -(2*a*c)/(a*(b+r))
    x2 = -(b+r)/(2*a)
    return [x2,x1]

print('Check that the three methods with a = 2, b = -1 and c = -3 give the same result')
print(corrSol(2,-1,-3))
print(sol1(2,-1,-3))
print(sol2(2,-1,-3))

print('Check the two methods with given numbers')
print(sol1(0.001,1000,0.001))
print(sol2(0.001,1000,0.001))
print('They both obtain two wrong results!')
print('The problem is the term -b + sqrt(b^2-4ac) that appears on the numerator of x2  in sol1 and on the denominaror of x1 in sol2')
print('The correct one, avoiding that subtraction, is the following: ')
print(corrSol(0.001,1000,0.001))

print('Actually using numpy: ')
print(np.roots([0.001,1000,0.001]))
#the problem is the term -b + sqrt(b^2-4ac) that appears on the numerator of x2  in sol1 and on the denominaror of x1 in sol2