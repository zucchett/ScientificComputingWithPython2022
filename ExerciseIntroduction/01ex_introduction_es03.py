import math

u_list = []
v_list = []

u_list = [float(item) for item in input("Enter the coordinates of the first point as x,y: ").split(",")]
v_list = [float(item) for item in input("Enter the coordinates of the second point as x,y: ").split(",")]
print()

u = (*u_list,)
v = (*v_list,)

distance = math.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)

print("The Euclidean distance between the points is: ", distance)
print()
