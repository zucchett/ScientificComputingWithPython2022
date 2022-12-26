##Computing the Euclidean distance between 2 points

import math
d = int
u = input("Enter the values in 2D space of the first point seperating with a comma ',' :")
v = input("Enter the values in 2D space of the first point seperating with a comma ',' :")
tuple_u = (u.split(',')[0],u.split(',')[1])
tuple_v = (v.split(',')[0],v.split(',')[1])
print(u,v)
print(tuple_u , tuple_v)

d = math.sqrt(math.pow(int(tuple_v[0]) - int(tuple_u[0]),2) + math.pow(int(tuple_v[1]) - int(tuple_u[1]),2))
print("Distance between 2 points is : %.2f" % d)
