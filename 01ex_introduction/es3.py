from math import sqrt # import square root from the math module
# the x and y coordinates are the points on the Cartesian plane
x1,x2,y1,y2=0,0,0,0
x1=input()
x1=int(x1)
x2=input()
x2=int(x2)
y1=input()
y1=int(y1)
y2=input()
y2=int(y2)
pointA = (x1, y1) # first point
pointB = (x2, y2) # second point
def calc_distance(p1, p2): # simple function, I hope you are more comfortable
  return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
distance = calc_distance(pointA, pointB) # here your beautiful result
print(distance)