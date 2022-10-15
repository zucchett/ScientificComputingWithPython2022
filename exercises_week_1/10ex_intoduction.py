#10. Normalization of a N-dimensional vector

import math

vector = [5,7,3,2,5]
norm = 0

#calculate the norm
for i in range(len(vector)):
    norm += vector[i]**2
norm = math.sqrt(norm)

i=0
while i<len(vector):
    vector[i] = round(vector[i]/norm,2)
    i += 1

tuple(vector)
print(f"The normalized vector is: {vector}")