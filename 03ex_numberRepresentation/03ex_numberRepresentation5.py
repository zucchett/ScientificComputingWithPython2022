# 5. Quadratic solution

import math
a = 0.001
b = 1000

def quadratic_sol(a,b,c):
    r = math.sqrt(b*b - 4*a*c)
    return ((-b+r)/(2*a), (-b-r)/(2*a))

print("a =", quadratic_sol(a,b,a))

#b)
def quadratic_re_expres(a,b,c):
    r = math.sqrt(b*b - 4*a*c)
    return (2*c/(-b-r), 2*c/(-b+r))
print("b =", quadratic_re_expres(a,b,a))

# The quadratic equation violated the cardinal rule of numerical analysis that says that # you have to avoid subtracting nearly equal numbers.
# This means that the more similar two numbers are, the more precision you can lose from subtracting them.

#c)

def quadratic_all(a,b,c):
    r = math.sqrt(b**2 - 4*a*c)
    return (2*c/(-b-r), (-b-r)/(2*a))
print("c =", quadratic_all(a,b,a))