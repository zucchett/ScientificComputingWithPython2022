import cmath

# (a)
a = 0.001
b = 1000
c = 0.001
print("Quadratic equation is : ", a, "*x^2 + ", b, "*x + ", c)

# calculate the discriminant
discriminant = (b ** 2) - (4 * a * c)
sol1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
sol2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
print("The solutions are", sol1, "and", sol2)

# (b)
# multiply by -b+sqrt(b^2-4ac) -b-sqrt(b^2-4ac)

re_express = (-b - cmath.sqrt(discriminant))
discriminant = (b ** 2) - (4 * a * c)
sol1 = (-b - cmath.sqrt(discriminant) * re_express) / (2 * a * re_express)
sol2 = (-b + cmath.sqrt(discriminant) * re_express) / (2 * a * re_express)
print("The new solutions are", sol1, "and", sol2)

# (c)  compute the roots of the quadratic equation correctly in all cases
a = 0.001
b = 1000
c = 0.001
print("Quadratic equation is : ", a, "*x^2 + ", b, "*x + ", c)
discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    num_roots = 2
    sol1 = (((-b) + cmath.sqrt(discriminant)) / (2 * a))
    sol2 = (((-b) - cmath.sqrt(discriminant)) / (2 * a))
    print("There are 2 roots: ", sol1, sol2)
elif discriminant == 0:
    num_roots = 1
    x = (-b) / 2 * a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, if the discriminant is < 0")
