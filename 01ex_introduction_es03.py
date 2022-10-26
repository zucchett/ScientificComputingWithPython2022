import math
x1 = input("enter x1:")
y1 = input("enter y1:")
x2 = input("enter x2:")
y2 = input("enter y2:")
t1 =( int(x1),int(y1))
t2 = (int(x2),int(y2))
##t1=(3,0)
##t2 =(0,4)

d = ((t2[0]-t1[0])**2)+((t2[1]-t1[1])**2)
distance = math.sqrt(d)
print("The euclidean distance between two points is:" ,distance)

