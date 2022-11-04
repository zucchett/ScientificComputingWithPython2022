import math
u=[]
v=[]
u = tuple(map(int, input("Enter two values for u (Please put an space betwwen the two variables i.e. '7 8'): ").split()))
v = tuple(map(int, input("Enter two values for v (Please put an space betwwen the two variables i.e. '7 8'): ").split()))

dist=math.sqrt(pow(abs(u[0]-v[0]),2)+pow(abs(u[1]-v[1]),2))
print(type(u))
print(type(v))
print(type(dist))

print("Distance between u and v is:", dist )
