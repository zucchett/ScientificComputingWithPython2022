from math import sqrt
u=(3,0)
v=(0,4)

def distance(u,v):
    return sqrt((u[0] - v[0])**2 + (u[1] + v[1])**2)

print('The distance between u = {} and v = {} is {} '.format(u,v, distance(u,v)))
