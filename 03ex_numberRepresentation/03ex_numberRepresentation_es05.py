# 5. Quadratic solution

# Write a function that takes in input three parameters ,
# and  and prints out the two solutions to the quadratic equation 
# using the standard formula:
 

# (a) use the function to compute the solution for
#  and 

# (b) re-express the standard solution formula by
#  multiplying the numerator and the denominator by 
# and again find the solution for ,  and . How does 
# it compare with what has been previously obtained,
# and why? (add the answer to a Python comment)

# (c) write a function that computes the roots of
# a quadratic equation accurately in all cases

import math

# point a
def quadratic_equ(a, b, c):
    print("Quadratic equation function: version 1")
    if((b**2) - (4*a*c)) < 0:
        print("Delta is less than 0")
        return
    x1 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    print("The first root is " + str(x1))
    print("The second root is " + str(x2))

# point b
def quadratic_equ_2(a, b, c):
    print("Quadratic equation function: version 2")
    if((b**2) - (4*a*c)) < 0:
        print("Delta is less than 0")
        return
    x1 = ((-b + math.sqrt((b**2) - (4*a*c)))/(2*a))*(-b - math.sqrt(b**2 - 4*a*c))/(-b + math.sqrt(b**2 - 4*a*c))
    x2 = ((-b - math.sqrt(b**2 - 4*a*c))*(-b + math.sqrt(b**2 - 4*a*c)))/((2*a)*(-b - math.sqrt(b**2 - 4*a*c)))
    print("The first root is " + str(x1))
    print("The second root is " + str(x2))

quadratic_equ(0.001, 1000, 0.001)

quadratic_equ_2(0.001, 1000, 0.001)

# we obtain different results because of the cancellation error
# this means that we are subtracting two numbers that are very close to one another

# let us define a new function

def quadratic_no_canc(a, b, c):
    print("Quadratic equation function: version 3 without cancellation error")
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print("Delta is less than 0")
        return
    if b > 0:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = c/(a*x1)
    else:
        x2 = (-b + math.sqrt(delta))/(2*a)
        x1 = c/(a*x1) 
    print("The first root is " + str(x1))
    print("The second root is " + str(x2))

quadratic_no_canc(0.001, 1000, 0.001)

# exercise done!


    

