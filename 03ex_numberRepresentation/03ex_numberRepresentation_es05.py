import math 
import sys
import cmath
def quadsolex(a,b,c):
	x1=(-b+cmath.sqrt((b**2)-4*a*c))/(2*a)
	x2=(-b-cmath.sqrt((b**2)-4*a*c))/(2*a)
	return x1,x2

def quadsol1(a,b,c):
	x1=(-b+math.sqrt((b**2)-4*a*c))/(2*a)
	x2=(-b-math.sqrt((b**2)-4*a*c))/(2*a)
	return x1,x2

def quadsol2(a,b,c):
	n1=(-b+math.sqrt((b**2)-4*a*c))*(-b-math.sqrt((b**2)-4*a*c))
	n2=(-b-math.sqrt((b**2)-4*a*c))*(-b+math.sqrt((b**2)-4*a*c))
	d1=2*a*(-b-math.sqrt((b**2)-4*a*c))
	d2=2*a*(-b+math.sqrt((b**2)-4*a*c))
	x1=n1/d1
	x2=n2/d2
	return x1,x2
print("Solutions with the first function:")
x=quadsol1(0.001,1000,0.001)
print(x)
print("Solutions with the second function:")
y=quadsol2(0.001,1000,0.001)
print(y)
print("Solutions with the third function (also valid for negative discriminant):")
z=quadsolex(-1,-1,2)
print(z)
#ANSWER: the result in (b) is close to the one in (a), but slightly off
#It's because the number is represented in the machine with a limited amount of bits, every time we multiply or
#divide for that number we introduce another approximation in the result
