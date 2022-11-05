# 32-bit floating point number

def confloat(x):

	# Check if input is a 32 bit string
	aux = "01"
	isBinary = True
	for c in str(x):
		if c not in aux:
			isBinary = False
			break
		else:
			pass    	
	if isBinary is False:
		return "Input string is not a binary string."
	if len(str(x)) < 32:
		print("Input string is shorter than 32 bits. Adding zeros at the end of the string to make it 32 bits.")
		aux = str(x)
		while len(aux) < 32:
			aux = aux + "0"
		x = int(aux)
	elif len(str(x)) > 32:
		return "Input string is longer than 32 bits."
	
	# Converting the binary string from decimal integer to binary representation
	bux = str(x)
	y = int(bux,2)
	
	# First digit (Sign)
	mask1 = 2147483648
	shift1 = 31
	sign = (y & mask1) >> shift1
	if sign:
		sign = -1
	else:
		sign = +1
		
	# Exponent
	mask2 = 2139095040
	shift2 = 23
	exp = (y & mask2) >> shift2
	
	# Mantissa
	mask3 = 8388607
	mant = y & mask3
	
	# Adding zeros to the left of the mantissa string to match the number of the mantissa bits (23) in case the first digits were zero and therefore cut
	dux = str(bin(mant))
	if len(dux) < 25:
		dux = dux.replace("b","b0")
	
	# Evaluating mantissa	
	i = -1
	cux = 1
	for n in dux:
		if i >= 1:
			cux += int(n)/(2**i)
		i += 1
	
	deci = float(cux)
	
	# Assemble
	mynum = sign * deci * 2**(exp-127)
	
	return mynum
	

a = input("Insert 32 bit binary string (e.g. 110000101011000000000000): ")
#110000101011000000000000
b = confloat(a)
if type(b) is float:
	print("The decimal representation of the single precision floating point number is " + str(b) +"." )
else:
	print("Couldn't convert to float. Maybe invalid input?")
