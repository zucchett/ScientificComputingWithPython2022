import math
x1 = input("u(x)= ")
y1 = input("u(y)= ")
x2 = input("v(x)= ")
y2 = input("v(y)= ")
u = (x1,y1)
v = (x2,y2)
D = (int(u[0])-int(v[0]))**2 + (int(u[1])-int(v[1]))**2
print ('the distance between x and y is :',math.sqrt(D))