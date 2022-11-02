#10. Normalization of a N-Dimensional Vector
import math
vector = [1,2,3,4,5]

sumOfComponents = 0

for i in vector:
    sumOfComponents += i*i

magnitude = math.sqrt(sumOfComponents)
normalVector = [x/magnitude for x in vector]

print(magnitude)
print(normalVector)