# Computing the distance

import math
    
u1 = float(input("Insert x coordinate of u vector: "))
u2 = float(input("Insert y coordinate of u vector: "))
v1 = float(input("Insert x coordinate of v vector: "))
v2 = float(input("Insert y coordinate of v vector: "))

u = (u1,u2)
v = (v1,v2)

result = math.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)
print("The euclidean distance between the two points is: ",result)