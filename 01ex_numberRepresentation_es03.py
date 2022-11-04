import math


def euclidean_distance(u, v):
    d= math.sqrt( abs((u[0]-v[0])**2 + (u[1]-v[1])**2) )
    return d

u=(3,0) 
v=(0,4)

distance = euclidean_distance(u, v)

print('euclidean distance among u=(3,0) and v=(0,4) is:', distance)
