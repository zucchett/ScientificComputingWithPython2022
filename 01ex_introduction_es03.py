import math
def distance():
    ux , uy , vx , vy = float(input("insert X of U: "))  ,float(input("insert Y of U: "))  ,float(input("insert X of V: "))  ,float(input("insert Y of V: ")) 
    dis=math.sqrt((float(ux)-float(vx))**2 + (float(uy)-float(vy))**2)
    print(dis)
distance()