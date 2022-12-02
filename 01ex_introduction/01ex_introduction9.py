# 9. Nested list comprehension
# A Pythagorean triple is an integer solution to the Pythagorean theorem  𝑎2+𝑏2=𝑐2 . The first Pythagorean triple is (3, 4, 5).
# Find and put in a tuple all unique Pythagorean triples for the positive integers  𝑎 ,  𝑏  and  𝑐  with  𝑐<100 .

py_triple = []

# (py_triple.append((a,b,c) for n in range(1,m+1)  )

##Nested List comprehension
n = 100
triples = [(a, b, c) for a in range(1, n) for b in range(a, n) for c in range(b, n) if a**2 + b**2 == c**2]
print(triples,'\n')
print(len(triples))