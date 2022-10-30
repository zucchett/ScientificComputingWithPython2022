# 5. Quadratic solution

# Write a function that takes in input three parameters $a$, $b$ and $c$ and prints 
# out the two solutions to the quadratic equation $ax^2+bx+c=0$ using the standard 
# formula:
# $$
# x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
# $$

# (a) use the function to compute the solution for $a=0.001$, $b=1000$ and $c=0.001$

# (b) re-express the standard solution formula by multiplying the numerator and the 
# denominator by $-b\mp\sqrt{b^2-4ac}$ and again find the solution for $a=0.001$, 
# $b=1000$ and $c=0.001$. How does it compare with what has been previously obtained,
# and why? (add the answer to a Python comment)

# (c) write a function that computes the roots of a quadratic equation accurately in 
# all cases

from math import sqrt

def quadratic_eq(a, b, c):
    x1 = (-b + ((b*b - 4*a*c)**(1/2))) / (2*a)
    x2 = (-b - ((b*b - 4*a*c)**(1/2))) / (2*a)
    print("x1: "+ str(x1))
    print("x2: "+ str(x2))

#a)
a = 0.001
b = 1000
c = 0.001
print("a: "+str(a)+ " b: "+ str(b)+ " c: "+str(c))
quadratic_eq(a, b, c)
print("")
def quadratic_eq2(a, b, c):
    x1_1 = ((-b + (b*b - 4*a*c)**(1/2)) * (-b + ((b*b - 4*a*c)**(1/2)))) / ((2*a) * (-b + ((b*b - 4*a*c)**(1/2))))
    x1_2 = ((-b + (b*b - 4*a*c)**(1/2)) * (-b - ((b*b - 4*a*c)**(1/2)))) / ((2*a) * (-b - ((b*b - 4*a*c)**(1/2))))
    x2_1 = ((-b - (b*b - 4*a*c)**(1/2)) * (-b + ((b*b - 4*a*c)**(1/2)))) / ((2*a) * (-b + ((b*b - 4*a*c)**(1/2))))
    x2_2 = ((-b - (b*b - 4*a*c)**(1/2)) * (-b - ((b*b - 4*a*c)**(1/2)))) / ((2*a) * (-b - ((b*b - 4*a*c)**(1/2))))
    print("x1_1: "+ str(x1_1))
    print("x1_2: "+ str(x1_2))
    print("x2_1: "+ str(x2_1))
    print("x2_2: "+ str(x2_2))

#b)
print("a: "+str(a)+ " b: "+ str(b)+ " c: "+str(c))
quadratic_eq2(a, b, c)
print("")
# Results are changed only in one case of x2 
# x2 in first function = -999999.999999
# x2 in second function (only in one case) = -999999.9999990001
# because float numbers can only have a limited number of meaningful decimal places

#c)
def calculate_roots(a, b, c):
    d = (b**2) - (4*a*c)
    x1 = (-b+sqrt(d))/(2*a)
    x2 = (-b-sqrt(d))/(2*a)
    print("x1: "+ str(x1))
    print("x2: "+ str(x2))

print("a: "+str(a)+ " b: "+ str(b)+ " c: "+str(c))
calculate_roots(a, b, c)
