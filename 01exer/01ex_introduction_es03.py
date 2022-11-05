#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import math
try:
    c = float(input("x1= "))
    d = float(input("x2 ="))
    e = float(input("y1 ="))
    f = float(input("y2 ="))
    dist = math.sqrt((c+d)**2+(e+f)**2)
    print("The distance between the two points is = ", dist)
except:
    print("Invalid characters")