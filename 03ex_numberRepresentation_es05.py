import math

def Quadratic_solution(a, b, c):
    
    sol1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    sol2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    print("First solution of quadratic equation is : ", sol1)
    print("Second solution of quadratic equation is : ", sol2)
    
#part a:
Quadratic_solution(0.001, 1000, 0.001)

#part b:
def modified_Quadratic_solution(a, b, c):
    
    modified_sol1 = -2 * c / (-b - math.sqrt(b**2 - 4*a*c))
    modified_sol2 = 2 * c / (-b + math.sqrt(b**2 - 4*a*c))
    print("\nFirst solution of quadratic equation after multiplying the numerator and denominator is : ", modified_sol1)
    print("Second solution of quadratic equation after multiplying the numerator and denominator is : ", modified_sol2)

modified_Quadratic_solution(0.001, 1000, 0.001)

'''
b is greater than a and c, the actual value of  sqrt(b**2-4*a*c) can be formally approximated in the form b+delta.
The division between very small numbers tipically leads to unstable results. Let  denote x1, x2 the solutions computed by the Quadratic_solution function, and  y1, y2 the solutions computed by the rationalized function.  x1 does not lead to division between small numbers. Instead, x2, performs the division between very small values, which leads to unstable behaviour.

y1 = 2*c/ delta --> unstable
y2= -c/b
'''
#part c:
def optimal_solution(a, b, c):

    opt_sol1 = -2*c / (b + math.sqrt(b**2 - 4*a*c))
    opt_sol2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a) 
    print("\nOptimal solution of quadratic equation is (first root): ", opt_sol1)
    print("Optimal solution of quadratic equation is (second root): ", opt_sol2)
               
optimal_solution(0.001, 1000, 0.001)

