#Assumption : all elements of vector are integers. This of course can change.
import math
n = input("Enter N (size of vector) : ")
vector = []
for i in range(int(n)):
    v = input("Enter next element of vector : ")
    vector.append(float(v))
print("Vector :",vector)
print()

#Normalized = x / sqrt(x**2)
r = math.sqrt(sum([x**2 for x in vector]))
normalized_vector = []
for v in vector:
    normalized_vector.append(v/r)
print("Normalized vector :", normalized_vector)