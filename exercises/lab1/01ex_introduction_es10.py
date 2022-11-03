# Normalization of a N-dimensional vector

import random
import math

vec = [2,35,256,74,34,99,136,228]
norm = 0

for x in vec:
	norm = norm + x**2

norm = math.sqrt(norm)

vec_norm = []
for x in range(len(vec)):
    vec_norm.append((vec[x]) / norm)

print("Vector: " + str(vec))
print("Norm " + str(norm))
print("Vector Normalized: " + str(vec_norm))

#Calculate norm of new vector
norm_new = 0
for x in vec_norm:
	norm_new = norm_new + x**2

print("Norm of the normalized vector: " +str(norm_new))
