import math

def distance_func(u,v):
    delta_x = u[0] - v[0]
    delta_y = u[1] - v[1]
    euclidean = math.pow(math.pow(u[0] - v[0], 2) + math.pow(u[1] - v[1], 2), 0.5)
    print(euclidean)

u = (3, 0)
v = (0, 4)
distance_func(u,v)

