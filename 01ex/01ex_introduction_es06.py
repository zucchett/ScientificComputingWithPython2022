# Casting

x = input("Insert first element: ")
y = input("Insert second element: ")

try:
	x = float(x)
	if x-int(x) == 0:
		x = int(x)
except:
	pass
	
try:		
	y = float(y)
	if y-int(y) == 0:
		y = int(y)
except:
	pass

print("type(x) = " + str(type(x)) + ", type(y) = " + str(type(y)))

try:
	z = x + y
	print("Operation successful: result is \"" + str(z) + "\".")
except:
	print("Operation failed.")
