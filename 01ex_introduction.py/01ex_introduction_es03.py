#Computing the distance

import math

def distance():
    ux = input("Enter X of U: ")
    uy = input("Enter Y of U: ")
    vx = input("Enter X of V: ")
    vy = input("Enter Y of V: ")

    dist = math.sqrt((float(ux)-float(vx))**2 + (float(uy)-float(vy))**2)
    print(dist)
distance()