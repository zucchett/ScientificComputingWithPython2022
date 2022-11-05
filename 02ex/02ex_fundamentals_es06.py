# Nested functions

import decimal as d

def square(x):
	return x**2
def cube(x):
	return x**3
	
num = input("Insert number: ")
try:
	num = int(num)
except:
	try:
		num = d.Decimal(num)	# if Decimal is not ok, just replace d.Decimal with float
	except:
		print("Not a valid number.")
		exit()
	
pwr = square(cube(num))
print("Input variable: " + str(num))
print("Elevated to the sixth power: " + str(pwr))

# Used Decimal from decimal module instead of float because often the values resulted inaccurate due to floating point errors
