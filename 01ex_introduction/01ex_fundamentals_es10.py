# 10. Normalization of a N-dimensional vector

# Write a program that takes an N-dimensional vector,
# e.g. a variable-length tuple of numbers,
# and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

import math

vector = []
sum = 0

dimension = int(input("Insert N, the dimension of the vector: "))
for i in range(1,dimension+1) :
    vector.append(int(input("Insert the " + str(i) + "-th component of the vector: " )))
    sum += vector[i-1]**2

norm_factor = math.sqrt(sum)
norm_vector = [vector[i]/norm_factor for i in range(0, dimension)]

print("The original " + str(dimension) + "-dimensional vector is: " + str(vector))
print("The normalized " + str(dimension) + "-dimensional vector is: " + str(norm_vector))
