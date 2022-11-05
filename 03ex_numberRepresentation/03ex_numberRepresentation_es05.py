import numpy as np
import math
a = .001
b = 1000
c = .001
def do_math(a,b,c):
    x1 = (-b + math.sqrt(pow(b,2) - (4*a*c))) / (2* a)
    x2 = (-b - math.sqrt(pow(b,2) - (4*a*c))) / (2* a)
    return x1,x2

def do_math2(a,b,c):
    fix_part = math.sqrt(pow(b,2) - (4*a*c))
    x1 = (-b + fix_part )*(-b - fix_part) / (2* a)/(-b - fix_part) 
    x2 = (-b - fix_part)*(-b + fix_part) / (2* a)/(-b + fix_part)
    return x1,x2

def accurate_math(a,b,c):
    a = np.float128(a)
    b = np.float128(b)
    c = np.float128(c)
    fix_part = math.sqrt(pow(b,2) - (4*a*c))
    x1 = (-b + fix_part )*(-b - fix_part) / (2* a)/(-b - fix_part) 
    x2 = (-b - fix_part)*(-b + fix_part) / (2* a)/(-b + fix_part)
    return x1,x2


x1,x2 = do_math(a, b, c)
print("The solution is:\nx1 = ", x1,"\nx2 = ",x2)

#Answer: Because in re-expressed equation , the value of numerator and denumenator has been multiplied by a factor, we can do the math more accurate.
x1,x2 = do_math2(a, b, c)
print("-------------------------------------------------------")
print("The re-expressed solution is:\nx1 = ", x1,"\nx2 = ",x2)

#As an accurate solution I changed the types of a, b, c to float128 in order to increase the accuracy even more.
x1,x2 = accurate_math(a, b, c)
print("-------------------------------------------------------")
print("The accurate solution is:\nx1 = ", x1,"\nx2 = ",x2)
