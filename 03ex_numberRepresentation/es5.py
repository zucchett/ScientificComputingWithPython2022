#first task 

import math


def quadratic(a, b, c):

    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)

    return x1, x2

print(quadratic(0.001, 1000, 0.001))

#second task
def quadratic_b(a, b, c):
    
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) * (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a) * (-b - math.sqrt(b * b - 4 * a * c))
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) * (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a) * (-b + math.sqrt(b * b - 4 * a * c))
    
    return x1, x2
    
print(quadratic_b(0.001, 1000, 0.001))

#results obtained is not the same, for the same expression we obtained different decimals due to computer arithmetic.
#!!!when using floating point numbers algorithms with the equivalent algebratic expressions may give different results !!!.



#third task
def quadratic_root(a, b, c):
    
    x1 = math.fsum([-b, math.sqrt(b * b - 4 * a * c)]) / (2 * a)
    x2 = math.fsum([-b, -math.sqrt(b * b - 4 * a * c)]) / (2 * a)
    
    return x1, x2

print(quadratic_root(0.001, 1000, 0.001))