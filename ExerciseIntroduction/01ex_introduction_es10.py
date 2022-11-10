"""
10. Normalization of a N-dimensional vector
Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one
(in such a way that the squared sum of all the entries is equal to 1).
"""
import math
vector = []
sum1 = 0
vector = [int(item) for item in input("Enters the vectors components separated only by commas : ").split(",")]
print()

for i in range(len(vector)):
    sum1 = sum1 + vector[i] ** 2

norm = math.sqrt(sum1)

vector_normalized = [vector[i] / norm for i in range(len(vector))]

print("The norm of your vector is: ", norm)
print()
print("The normalized vector is: \n", vector_normalized)
print()

sum2 = 0
for i in range(len(vector_normalized)):
    sum2 = sum2 + vector_normalized[i] ** 2

norm2 = math.sqrt(sum2)

print("The norm of this new vector is: ", norm2)
print()
