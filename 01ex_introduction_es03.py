import math
def distance():
    ux , uy , vx , vy = input("\ninsert X of U: ") , input("insert Y of U: ") , input("insert X of V: ") , input("insert Y of V: ")
    distance=math.sqrt((float(ux)-float(vx))**2 + (float(uy)-float(vy))**2)
    print(f"\nThe euclidean distance between u and v is: {distance}\n")
    
distance()