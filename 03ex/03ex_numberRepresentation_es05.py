# Quadratic solution
import math as m

def standard(at,bt,ct):
	delta = m.sqrt(bt**2-4*at*ct)
	rad1 = (-bt-delta)/(2*at)
	rad2 = (-bt+delta)/(2*at)
	std = [rad1, rad2]
	return std

def rewrite(at,bt,ct):
	delta = m.sqrt(bt**2-4*at*ct)
	radw1 = (2*ct)/(-bt+delta)
	radw2 = (2*ct)/(-bt-delta)
	rwt = [radw1, radw2]
	return rwt
	
def stable(at,bt,ct):
	delta = m.sqrt(bt**2-4*at*ct)
	rads1 = (-bt-delta)/(2*at)
	rads2 = (2*ct)/(-bt-delta)
	stb = [rads1, rads2]
	return stb
	

print("Quadratic function ax**2+bx+c")

# Input
a = input("Insert \"a\" parameter: ")
b = input("Insert \"b\" parameter: ")
c = input("Insert \"c\" parameter: ")

# Check if input are valid numbers
try:
	a = float(a)
	b = float(b)
	c = float(c)
except:
	pass

if (type(a) is not float) or (type(b) is not float) or (type(c) is not float):
	print("Invalid parameter.")
	exit()

# Functions

print("The two solutions using standard formula are: " + str(standard(a,b,c)))
print("The two solutions using rewritten formula are: " + str(rewrite(a,b,c)))
print("The two solutions using stable formula are: " + str(stable(a,b,c)))

# The results calculated with the two methods are slightly different; the algorithm is unstable due to the presence of a catastrophic cancellation (-b+delta) in "rad2" (standard formula with + sign) and "rad1w" (rewritten formula with + sign)
# Therefore if we calculate the two radicals using the two expressions without catastrophic cancellation we obtain two stable solutions
