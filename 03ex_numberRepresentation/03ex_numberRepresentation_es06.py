import math

def func(x):
	return x*(x-1)

delta=1e-2
res=(func(1+delta)-func(1))/delta
print(res)
delta=delta/100
while delta>=1e-14:
	res=(func(1+delta)-func(1))/delta
	print(res)
	delta=delta/100
#The analytical result of the limit in x=1 is 1, the result of the program with delta=0.01 is different
#because of the definition of the derivative: as delta gets closer to 0 the formula gives results that are closer 
#to the real value (delta=10e-2 is not small enough to get a good approximation of the result)
#as delta decreases (gets smaller than 10e-10) we notice that the output of the function drifts away from the
#analytical result. This is due to the machine precision limit: it can only store values with a limited amount of bits
#in the mantissa field, so every computation involving delta will introduce an approximation that gets bigger as
#delta diminishes
