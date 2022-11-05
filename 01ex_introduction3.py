import math
x1,x2=input("Please give cordinates for the first point")+ input()
x=(int(x1),int(x2))
print ("The first point is" ,x)

y1,y2=input("Please give cordinates for the second point")+ input()
y=(int(y1),int(y2))
print ("The second point is",y)

d =(math.sqrt(math.pow((int(y1)-int(x1)),2) + math.pow((int(y2)-int(x2)),2)))
print("The euclidean distance between two points is " , d)