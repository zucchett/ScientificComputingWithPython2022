# Number representation

def convert(xa, i, f):

	if i == 2 or i == 16:
		xa = int(xa)
		
	if f == 2:
		xa = bin(xa)
		xa = xa.replace("0b","")
	elif f == 16:
		xa = hex(xa)
		xa = xa.replace("0x","")
		
	return xa



t = 0
invalidType = True	
while(invalidType):
	t = input("Insert input variable representation (binary=2, decimal=10, hexadecimal=16): ")
	try:
		t = int(t)
	except:
		pass
	if t == 2 or t == 10 or t == 16:
		invalidType = False
	else:
		print("You must insert 2, 10 or 16.")

x = 0
xi = 0.
invalidValue = True
while(invalidValue):
	x = input("Insert integer input variable: ")
	if t == 10:
		try:
			xi = int(x)
		except:
			pass
		if type(xi) is int:
			invalidValue = False
		else:
			print("Insert an integer.")
	elif t == 2:
		try:
			xi = int(x,2)
		except:
			pass
		if type(xi) is int:
			invalidValue = False
		else:
			print("Insert a valid binary number.")
	elif t == 16:
		try:
			xi = int(x,16)
		except:
			pass
		if type(xi) is int:
			invalidValue = False
		else:
			print("Insert a valid hexadecimal number.")

u = 0
invalidType2 = True	
while(invalidType2):
	u = input("Insert output variable representation (binary=2, decimal=10, hexadecimal=16): ")
	try:
		u = int(u)
	except:
		pass
	if u == 2 or u == 10 or u == 16:
		invalidType2 = False
	else:
		print("You must insert 2, 10 or 16.")

c = convert(xi,t,u)
# Not sure if you meant "Determine input type in the function" as "fix it as an argument" or "check its type in the function"; I interpreted it in the first way since it makes more sense

print("The converted number is " + str(c) + ".")
