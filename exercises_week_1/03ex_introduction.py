#3. Computing the distance

import math


print("Insert two coordinates of the point A:")
ax = float(input())
ay = float(input())

print("Insert the coordinates of the point B:")
bx = float(input())
by = float(input())

#defining the two tuples
a_coordinates = (ax, ay)
b_coordinates = (bx, by)

try:
    distance = math.sqrt((bx-ax)**2+(by-ay)**2)
    distance = round(distance,2)
    print(f"The distance between point A({ax},{ay}) and point B({bx},{by}) is: {distance}")
except:
   print("One of the numbers is not valid")