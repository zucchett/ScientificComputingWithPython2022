#3.Computing the distance

from math import sqrt
def Distance(u,v):
    """Distance returns the euclidean distance between two 2D tuples"""
    return sqrt((u[0]-v[0])**2 + (u[1]-v[1])**2 )

#main
u=(3,0)
v=(0,4)
print("The Euclidean distance between u =",u,"and v =",v,"would be:", Distance(u,v))
