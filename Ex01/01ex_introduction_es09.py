#9. Nested List Comprehension

n = 100

pythagoreanTriples = [(a, b, c) for a in range(1, n + 1) for b in range(a, n + 1) for c in range(b, n + 1) if a**2 + b**2 == c**2]

print(pythagoreanTriples)
