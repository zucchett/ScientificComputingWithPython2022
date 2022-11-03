import math
def distance():
    ux , uy , vx , vy = float(input("enter X of U: ")) , float(input("enter Y of U: ")) , float(input("enter X of V: ")) , float(input("enter Y of V: "))
    dist_1=math.sqrt((float(ux)-float(vx))**2 + (float(uy)-float(vy))**2)
    print(dist_1)
distance()