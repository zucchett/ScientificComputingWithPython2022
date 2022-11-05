# Nested list comprehension

import math 

c = 1
pythagorean_triples = []
while c < 100:
    for i in range (1,10):
        for j in range (1,10):
            if math.pow(i,2) + math.pow(j,2) == math.pow(c,2):
                pythagorean_triples.append([i,j,c])
    c = c+1

print(pythagorean_triples)