import math

def euclidean_function(u, v):
    distance = (u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2
    result = math.sqrt(distance) 
    return(result)

x1 = int(input("Set the value of x1: "))
y1 = int(input("Set the value of y1: "))
x2 = int(input("Set the value of x2: "))
y2 = int(input("Set the value of y2: "))
        
u = (x1, y1)
v = (x2, y2)

print(euclidean_function(u, v))
