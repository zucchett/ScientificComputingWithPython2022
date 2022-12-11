import math 
u = (5,0)
v = (0,12)

x = math.pow(u[0] - v[0], 2) 
y = math.pow((int(u[1]) - int(v[1])), 2)
print(x)
print(y)

z = math.sqrt(x + y)
print(z)