# Casting

x = input("Insert first element: ")
y = input("Insert second element: ")

try:
	x = int(x)
except:
	try:
		x = float(x)
	except:
		pass
	pass
	
try:		
	y = int(y)
except:
	try:
		y = float(y)
	except:
		pass
	pass

print("type(x) = " + str(type(x)) + ", type(y) = " + str(type(y)))

try:
	z = x + y
	print("Operation successful: result is \"" + str(z) + "\".")
except:
	print("Operation failed.")
