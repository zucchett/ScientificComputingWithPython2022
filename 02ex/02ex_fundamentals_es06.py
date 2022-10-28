# Nested functions

import decimal as d

def square(x):
	return x**2
def cube(x):
	return x**3
	
num = input("Insert number: ")
try:
	num = d.Decimal(num)
	if num-int(num) == 0:
		num = int(num)
	pwr = square(cube(num))
	print("Input variable: " + str(num))
	print("Elevated to the sixth power: " + str(pwr))
except:
	print("Not a valid number.")
	
# Used Decimal from decimal module instead of float because often the values resulted inaccurate due to floating point errors
