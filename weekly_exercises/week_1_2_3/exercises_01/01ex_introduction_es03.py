#Zuccolo Giada, matr. 2055702
#EXE 3

import math

ux = int(input("POINT u\nx = "))
uy = int(input("y = "))
vx = int(input("\nPOINT v\nx = "))
vy = int(input("y = "))
distance = math.sqrt((ux-vx)**2 + (uy-vy)**2)
print("\nDistance = "+str(distance))
