#5. Quadratic solution

#Write a function that takes in input three parameters ,  and  and prints out the two solutions to the quadratic equation 
# using the standard formula:
 

#(a) use the function to compute the solution for ,  and 

#(b) re-express the standard solution formula by multiplying the numerator and the denominator by 
# and again find the solution for ,  and . How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)

#(c) write a function that com

# -------------------------------------- Code Begin-------------------------------------
from  cmath import sqrt 

def solver(a,b,c):
    d =(b**2) - (4*a*c)
    sol1 = (-b-sqrt(d))/(2*a)
    sol2 = (-b+sqrt(d))/(2*a)
    return sol1,sol1

def solverRe(a,b,c):
    d =(b**2) - (4*a*c)
    sol1 = ( b**2 - d ) / ((2*a) * (-b + sqrt(d)))
    sol2 = ( b**2 - d ) / ((2*a) * (-b - sqrt(d)))
    return sol1,sol1


a,b,c = 0.001,1000,0.001
print('----------------------- Question a ---------------------')
print('Solutions for the equation : ',a,'x² +',b,'x +',c,' are :', solver(a,b,c))
print('----------------------- Question b ---------------------')
print('Solutions for the equation : ',a,'x² +',b,'x +',c,' are :', solverRe(a,b,c))



