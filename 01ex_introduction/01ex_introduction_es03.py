#ex_03

#Write a function that calculates and returns the euclidean distance between two points u and v in a 2D space, 
#where u and v are both 2-tuples (x,y).

import math

u = (u1, u2)
v = (v1, v2)

distance = math.sqrt(math.pow(v1 - u1, 2) + math.pow(v2 - u2, 2))


u1 = int (input("Set the value of u1: ")) 
u2 = int (input("Set the value of u2: ")) 
v1 = int (input("Set the value of v1: "))
v2 = int (input("Set the value of v2: ")) 

print("%.6f"%distance)
