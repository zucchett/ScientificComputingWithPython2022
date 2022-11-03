"""
5. Write a function that takes in input three parameters $a$, $b$ and $c$ and prints out the two solutions to the
quadratic equation $ax^2+bx+c=0$ using the standard formula:
$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

(a) use the program to compute the solution for $a=0.001$, $b=1000$ and $c=0.001$

(b) re-express the standard solution formula by multiplying the numerator and the denominator by
$-b\mp\sqrt{b^2-4ac}$ and again find the solution for $a=0.001$, $b=1000$ and $c=0.001$.
How does it compare with what has been previously obtained, and why?

(c) write a function that computes the roots of a quadratic equation accurately in all cases
"""

import math

a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))

# a with math.sqrt
print("\nResults with math.sqrt:")
print("\na)\nx1 = ", (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
print("x2 = ", (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))

# b with math.sqrt
print("\nb)\nx1 = ", ((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)) * (-b + math.sqrt(b ** 2 - 4 * a * c)) / (
            -b + math.sqrt(b ** 2 - 4 * a * c)))
print("x2 = ", ((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)) * (-b - math.sqrt(b ** 2 - 4 * a * c)) / (
            -b - math.sqrt(b ** 2 - 4 * a * c)))

# a with **.5
print("\n\nResults with **.5:")
print("\na)\nx1 = ", (((-b + (b ** 2 - 4 * a * c)) ** .5) / (2 * a)))
print("x2 = ", (((-b - (b ** 2 - 4 * a * c)) ** .5) / (2 * a)))
# b with **.5
print("\nb)\nx1 = ", (((-b + (b ** 2 - 4 * a * c)) ** .5) / (2 * a)) * ((-b + (b ** 2 - 4 * a * c)) ** .5) / (
            (-b + (b ** 2 - 4 * a * c)) ** .5))
print("x2 = ", (((-b - (b ** 2 - 4 * a * c)) ** .5) / (2 * a)) * ((-b - (b ** 2 - 4 * a * c)) ** .5) / (
            (-b - (b ** 2 - 4 * a * c)) ** .5))

# I couldn't find the difference of point b

# c
print("\nc)\nResults with math.sqrt() and math.fsum():")
print("\nx1 = ", (math.fsum([-b, math.sqrt(b ** 2 - 4 * a * c)]) / (2 * a)))
print("x2 = ", (math.fsum([-b, -math.sqrt(b ** 2 - 4 * a * c)]) / (2 * a)))
