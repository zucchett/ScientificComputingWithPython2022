# Cubes

import math

#a)
cubes = []
for i in range(0, 11):
    cubes.append(math.pow(i,3))

print(cubes)

#b)
cubes2 = []
[cubes2.append(math.pow(x,3)) for x in range(0,11)]

print(cubes2)

