# 9. Nested list comprehension
# A Pythagorean triple is an integer solution to the Pythagorean theorem  . The first Pythagorean triple is (3, 4, 5).
# Find and put in a tuple all unique Pythagorean triples for the positive integers  a,  b and c   with c<100 .
from math import sqrt

pyth = []
for a in range(1, 100):
    for b in range(1, 100):
        c = int(sqrt(a * a + b * b))
        if c * c == a * a + b * b and a < b and a + b > c and b + c > a and a + c > b and c < 100:
            pyth.append((a, b, c))
tup = tuple(pyth)

print(pyth)
print(tup)

# pyth2 = [(a, b, c) for a in range(1, 100) for b in range(1, 100) for c in range(1,100) if c == int(sqrt(a * a + b * b)) and c * c == a * a + b * b and a < b and a + b > c and b + c > a and a + c > b]
# print(pyth2)