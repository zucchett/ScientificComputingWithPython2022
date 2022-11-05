import math
vector = (1, 4, 3, 6)
squareList = []
sum_Squares = 0
for i in vector:
    sum_Squares += i*i
length = math.sqrt(sum_Squares)
normList = []
for i in vector:
    normList.append(i/length)
print(" normalized vector : ", tuple(normList))

a = 0
for i in normList:
    a += i*i

print(" length of normalized vector: ", math.sqrt(a))