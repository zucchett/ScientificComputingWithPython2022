x = input("Insert first element: ")
y = input("Insert second element: ")

try:
	x = int(x)
except:
	try:
		x = float(x)
	except:
		pass

try:		
	y = int(y)
except:
	try:
		y = float(y)
	except:
		pass
try:
	z = x + y
	print("Results are: \"" + str(z) + "\".")
except:
	print("Please add the inputs correctly.")