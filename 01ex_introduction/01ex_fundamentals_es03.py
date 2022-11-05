# 3. Computing the distance

# Write a function that calculates and returns the euclidean distance between two points u and v in a 2D space, where u and v are both 2-tuples (x,y).

# Example: if u=(3,0) and v=(0,4), the function should return 5.

# Hint: in order to compute the square root, import the math library with import math and use math.sqrt().

import math

u1 = int(input("Set the value of u1: ")) # type Enter
u2 = int(input("Set the value of u2: ")) # type Enter
u = (u1, u2)

v1 = int(input("Set the value of v1: ")) # type Enter
v2 = int(input("Set the value of v2: ")) # type Enter
v = (v1, v2)

distance = math.sqrt((u1**2+v1**2)+(u2**2+v2**2))

print(distance)