# Excersize 3:
import math
u =input("Enter your first point as x,y: ")
u = tuple(map(int, u.split(',')))
print(u)
v =input("Enter your second point as x,y: ")
v= tuple(map(int, v.split(',')))
print(v)
d= math.sqrt(math.pow((v[0]-u[0]),2) + math.pow((v[1]-u[1]),2))
print("distance between two points is=%5.2f"%(d))

#With a function
def CalculateDistance(u, v):
    d= math.sqrt(math.pow((v[0]-u[0]),2) + math.pow((v[1]-u[1]),2))
    print("distance between two points which are alguments of this function is =%5.2f"%(d))

CalculateDistance((0,3), (4,0))
