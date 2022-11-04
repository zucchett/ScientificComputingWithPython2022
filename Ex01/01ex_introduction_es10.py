#10. Normalization of a N-Dimensional Vector
import math
# vector = [1,2,3,4,5]
vector = (1,2,3,4,5)  #input vector
sumOfComponents = 0

for i in list(vector):
    sumOfComponents += i*i

magnitude = math.sqrt(sumOfComponents)
normalVector = [x/magnitude for x in vector]

print("Magnitude:",magnitude)
print("Normal Vector:",normalVector)
print("Squared Sum of Normalalized Vector Components:",sum([x*x for x in normalVector]))