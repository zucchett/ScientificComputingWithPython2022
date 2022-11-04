import math

u1 = float(input("Enter the x coordinate of u "))
u2 = float(input("Enter the y coordinate of u "))
v1 = float(input("Enter the x coordinate of v "))
v2 = float(input("Enter the y coordinate of v "))

u=(u1,u2)
v=(v1,v2)

dist = math.sqrt((v1-u1)**2+(v2-u2)**2)
dist = round(dist,2)
print(f"The distance between point U({u1},{u2}) and point V({v1},{v2}) is: {dist}")
