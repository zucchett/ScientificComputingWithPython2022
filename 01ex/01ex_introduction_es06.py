# Casting

x = input("Insert first element: ")
y = input("Insert second element: ")

try:
<<<<<<< HEAD
	x = int(x)
except:
	try:
		x = float(x)
=======
	x = float(x)
except:
	try:
		x = int(x)
>>>>>>> main
	except:
		pass
	
try:		
<<<<<<< HEAD
	y = int(y)
except:
	try:
		y = float(y)
=======
	y = float(y)
except:
	try:
		y = int(y)
>>>>>>> main
	except:
		pass

print("type(x) = " + str(type(x)) + ", type(y) = " + str(type(y)))

try:
	z = x + y
	print("Operation successful: result is \"" + str(z) + "\".")
except:
	print("Operation failed.")
