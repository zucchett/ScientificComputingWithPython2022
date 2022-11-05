import math

def distance(u,v):
    eq = math.sqrt(u[0] ** 2 + v[1] ** 2) 
    return(eq)

u = (3,0)
print(type(u))
v = (0,4)
print(type(v))

print(distance(u,v)) 