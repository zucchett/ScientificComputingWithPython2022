#Quadratic solution
import math
import cmath

############ (a) ############

def Quadratic_solution(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
    return x1, x2
print('First solution:',Quadratic_solution(0.001,1000,0.001))

############ (b) ############

def Quadratic_solution_2(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c))*(-b + math.sqrt(b**2 - 4*a*c))/2*a*(-b + math.sqrt(b**2 - 4*a*c))
    x2 = (-b - math.sqrt(b**2 - 4*a*c))*(-b + math.sqrt(b**2 - 4*a*c))/2*a*(-b - math.sqrt(b**2 - 4*a*c))
    return x1, x2
print('Second solution:',Quadratic_solution_2(0.001,1000,0.001))

#we didn't find the same result because distributive law does not hold

############ (c) ############



def Quadratic_acc_sol(a,b,c):
    d = (b**2) - (4*a*c)
    x1 = (-b-cmath.sqrt(d))/(2*a)
    x2 = (-b+cmath.sqrt(d))/(2*a)
    return x1,x2

print('Accurate solution:',Quadratic_acc_sol(0.001,1000,0.001))
