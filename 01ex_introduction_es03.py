# # point u
# x1=3
# y1=0
# # point v
# x2=0
# y2=4
# distance=((x1-x2)**2+(y1-y2)**2)**0.5
# print(f'distance between points ({x1},{y1}) and ({x2,y2})is {distance}')

 #calculate distance with math library
import math
u=(3,0)
v=(0,4)
distance=math.dist(u,v)
print(distance) 