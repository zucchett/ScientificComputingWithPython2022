import math

vector = (1, 4, 2, 5)
squareList = []
sumOfSquares = 0
for x in vector:
    sumOfSquares += x*x
length = math.sqrt(sumOfSquares)

normList = []
for x in vector:
    normList.append(x/length)
print("The normalized vector is : ", tuple(normList))

a = 0
for i in normList:
    a += i*i

print("The length of the normalized vector: ", math.sqrt(a))
