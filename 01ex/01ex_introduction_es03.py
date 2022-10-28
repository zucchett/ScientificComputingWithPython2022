# Computing the distance

import math as m

try:
	x1 = float(input("Insert the x coordinate of the first point: "))
	y1 = float(input("Insert the y coordinate of the first point: "))
	x2 = float(input("Insert the x coordinate of the second point: "))
	y2 = float(input("Insert the y coordinate of the second point: "))
	x = (x1,y1)
	y = (x2,y2)
	d = m.sqrt((x1+x2)**2+(y1+y2)**2)
	print("The distance between the two points is " + str(d) + ".")
except:
	print("Invalid coordinate.")
