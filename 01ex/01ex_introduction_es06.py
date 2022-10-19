# Casting

x = input("Insert first element: ")
y = input("Insert second element: ")

try:
	x = float(x)
except:
	try:
		x = int(x)
	except:
		pass
	
try:		
	y = float(y)
except:
	try:
		y = int(y)
	except:
		pass

print("type(x) = " + str(type(x)) + ", type(y) = " + str(type(y)))

try:
	z = x + y
	print("Operation successful: result is \"" + str(z) + "\".")
except:
	print("Operation failed.")
