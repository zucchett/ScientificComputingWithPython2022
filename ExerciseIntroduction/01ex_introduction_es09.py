"""
9. Nested list comprehension

> A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is
(3, 4, 5).

Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.
"""

pythagoras = []

pythagoras = [(a, b, c) for a in range(1, 101) for b in range(a + 1, 101) for c in range(101) if
              a ** 2 + b ** 2 == c ** 2]

print("The Pythagorean triples are: \n", pythagoras)
print()
