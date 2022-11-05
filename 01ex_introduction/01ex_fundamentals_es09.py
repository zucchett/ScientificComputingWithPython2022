# 9. Nested list comprehension

# A Pythagorean triple is an integer solution to the Pythagorean theorem . The first Pythagorean triple is (3, 4, 5).

# Find and put in a tuple all unique Pythagorean triples for the positive integers ,  and  with .

import math

upper_bound = int(input("Set the upper bound, i.e. the hypotenuse maximum value: "))

Pyt_triples = [(c1, c2, hyp) for c1 in range(1, upper_bound) for c2 in range(c1, upper_bound) for hyp in range(c2, upper_bound+1) if c1**2 + c2**2 == hyp**2  ]

print("The Pythagorean triples with an hypothenuse maximum value of " + str(upper_bound) + " are: " + str(Pyt_triples))