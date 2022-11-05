import math

u = (4,0)
v = (0,4)

squaredSum = 0
euclideanDistance = 0

if len(u) == len(v):
    for i in range(len(u)):
        squaredSum += (u[i] - v[i])**2
    euclideanDistance = math.sqrt(squaredSum)
    print("Euclidean Distance: %.2f" % euclideanDistance)
else:
    print("Incompatible Dimensions of the point!")
