import math

def euclidean(u,v):
    distance = math.sqrt(((u[0]-v[0])**2)+((u[1]-v[1])**2))
    return distance

print(euclidean((0,6),(8,0)))