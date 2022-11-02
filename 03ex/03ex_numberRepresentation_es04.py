# Machine precision

a = 0 # Zero
b = 0 # a + e, compared to a to see if there was a difference
i = 0 # loop count, which also is the (opposite of the) exponent in the e expression
e = 0 # e from epsilon, gradually smaller quantity that is added to a
m = 0 # e of the previous loop

while True:
	e = 2**(-i)
	b = a + e
	print(i, e)
	if a == b:
		break
	else:
		b = 0
		m = e
	i += 1

print("Machine precision is " + str(m))
