#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
def conversion(x, b, e):

	if b == 2 or b == 16:
		x = int(x)

	if e == 2:
		x = bin(x)
		
	elif e == 16:
		x = hex(x)
		

	return x




InitialType = True	
while(InitialType):
	i = int(input("Insert the input representation among 2, 10 amd 16: "))
	#try:
	#	i = int(i)
	#except:
	#	pass
	if i == 2 or i == 10 or i == 16:
		InitialType = False
	else:
		raise ValueError('ERROR: The input representation is wrong!!!')

a = 0
y = 0.
invalidValue = True
while(invalidValue):
	a = input("Insert integer input variable: ")
	if i == 10:
		try:
			y = int(a)
		except:
			pass
		if type(y) is int:
			invalidValue = False
		else:
			print("Insert an integer.")
	elif i == 2:
		try:
			y = int(a,2)
		except:
			pass
		if type(y) is int:
			invalidValue = False
		else:
			print("The binary number is not correct.")
	elif i == 16:
		try:
			y = int(a,16)
		except:
			pass
		if type(y) is int:
			invalidValue = False
		else:
			print("The hexadecimal number is not correct.")


FinalType = True	
while(FinalType):
	f = int(input("Insert the output representation among 2, 10 and 16: "))
	#try:
	#	f = int(f)
	#except:
	#	pass
	if f == 2 or f == 10 or f == 16:
		FinalType = False
	else:
		raise ValueError('ERROR: The output representation is wrong!!!')

result =  conversion(y,i,f)

print("The number converted is " + str(result))
