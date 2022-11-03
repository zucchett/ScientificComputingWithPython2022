import math
x1 = float(input("Enter x1 : "))
y1 = float(input("Enter y1 : "))
p1 = (x1, y1)
print("p1 :", p1)
x2 = float(input("Enter x2 : "))
y2 = float(input("Enter y2 : "))
p2 = (x2, y2)
print("p2 :", p2)

d = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
print("distance of two points is : %.3f" % d)
