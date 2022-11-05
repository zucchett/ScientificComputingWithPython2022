import math
def distance():
    ux , uy , vx , vy = input("enter X of U: ") , input("enter Y of U: ") , input("enter X of V: ") , input("insert Y of V: ")
    distance=math.sqrt((float(ux)-float(vx))**2 + (float(uy)-float(vy))**2)
    print(distance)
distance()