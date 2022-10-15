import math
#9. Nested list comprehension

a=0
b=0
c=0

triples = [(c,b,a) for c in range(100) for b in range(1,c) for a in range(b) if c*c == b*b+a*a]
print(f"The Pithagorean triples from 0 to 100 are: {triples}")