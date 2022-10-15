# Normalization of a N-dimensional vector

import math as m

i = 0
v = []

try:
	n = int(input("Insert the dimensions of the vector: "))
	while i < n:
		aux = input("Insert the value of the coordinate " + str(i+1) + ": ")
		try:
			v.append(float(aux))
		except:
			print("Invalid input. Retry.")
			continue
		i += 1
	
	v2 = [v[int(i)]**2 for i in range(len(v))]	# Auxiliary vector with squared components
	r = m.sqrt(sum(v2))	# Length of the vector
	vr = [v[int(i)]/r for i in range(len(v))]	# Renormalised vector components

	print("The input vector is: " + str(v) + ", length " + str(r))
	print("The renormalized vector is: " + str(vr) + ", length " + str(m.sqrt(sum([vr[i]**2 for i in range(len(vr))]))))

except:
	print("Invalid input.")
