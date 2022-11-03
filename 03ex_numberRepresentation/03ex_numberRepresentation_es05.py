# 5. Quadratic solution

# Write a function that takes in input three parameters ,  and  and prints out the two solutions to the quadratic equation 
# using the standard formula:
 

# (a) use the function to compute the solution for ,  and 

# (b) re-express the standard solution formula by multiplying the numerator and the denominator by 
# and again find the solution for ,  and . How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)

# (c) write a function that computes the roots of a quadratic equation accurately in all cases

# -------------------------------------- Code Begin-------------------------------------

from  math import sqrt

a,b,c = 0.001,1000,0.001
print('----------------------- Question a ---------------------')
def solver(a,b,c):
    d =(b**2) - (4*a*c)
    sol1 = (-b-sqrt(d))/(2*a)
    sol2 = (-b+sqrt(d))/(2*a)
    return sol1,sol2

print('Solutions for the equation : ',a,'x² +',b,'x +',c,' are :', solver(a,b,c))

# Why the results are not correct or not very close to the true value?
# The quadratic equation violated the
# cardinal rule of numerical analysis: avoid subtracting
# nearly equal numbers. The more similar two numbers are,
# the more precision you can lose from subtracting them. In this
# case √(b² – 4ac) is very nearly equal to b.

print('----------------------- Question b ---------------------')

def solver_2(a,b,c):
    d =(b**2) - (4*a*c)
    sol1 = (2*c) / (-b + sqrt(d))
    sol2 = (2*c) / (-b - sqrt(d))
    return sol1,sol2

print('Solutions for the equation : ',a,'x² +',b,'x +',c,' are :', solver_2(a,b,c))
# the results are different due to the cancellation error,  because b^2 is
# much larger than 4ac, the square root is approximately equal to b. If b
# is positive and you add that positive square root to negative b, you get
# "cancellation", which gives a loss of numerical precision.

# the method used in question b is not also very correct, because we improved
# the results of (solu2) but
# we made the results of (sol1) much worse for same reason stated above :
# we subtracted two nearly equal numbers!
print('----------------------- Question c ---------------------')

# ******** Method #1 ********

def solver_3(a,b,c):  
    d = (b**2) - (4*a*c)  
    sqrt_val = sqrt(abs(d))  
    if d > 0:  
        print(" real and different roots ")
        return ((-b + sqrt_val) / (2 * a)),((-b - sqrt_val) / (2 * a)) 
    elif d == 0:  
        print(" real and same roots")
        return (-b / (2 * a))
    else:  
        print("Complex Roots")
        return complex((- b / (2 * a)),sqrt_val),complex((- b / (2 * a)),-sqrt_val)
    
# ******** Method #2 ********

from cmath import sqrt as csqrt

def solver_4(a,b,c):
    d =(b**2) - (4*a*c)
    sol1 = (-b-csqrt(d))/(2*a)
    sol2 = (-b+csqrt(d))/(2*a)
    return sol1,sol2

print('Method 1: Solutions for the equation : ',a,'x² +',b,'x +',c,' are :', solver_3(a,b,c))
print('Method 2: Solutions for the equation : ',a,'x² +',b,'x +',c,' are :', solver_4(a,b,c))


# -------------------------------------- Code End  -------------------------------------


