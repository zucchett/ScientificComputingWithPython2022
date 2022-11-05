#Zuccolo Giada, matr. 2055702
#EXE 10

import random
import math

dim = int(input("N-dim = "))

v = []
for x in range(dim):
    v.append(round(random.random(), 8))
print("Starting vector = \t"+str(v))

norm_value = 0
for x in range(dim):
    norm_value += (v[x])**2
for x in range(dim):
    v[x] = round((v[x]) / math.sqrt(norm_value), 8)

print("Normalized vector = \t" + str(v))
