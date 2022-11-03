# The derivative

def f(x):
	return x*(x-1)

def derivative_x(x,delta):
    return (f(x+delta)-f(x))/delta

x=1
delta=0.01
derivative = derivative_x(x,delta)

print("\nDerivative with delta = 10^-2 and x = 1: "+str(derivative))
print("Derivative analitically: "+str(float(x))+"\n")

# In the derivative formulation, delta tends to zero, while to perform 
# the calculation we must assign it a discrete value.
# With a smaller and smaller delta we approach to the correct result.

for i in range(4,15,2):
	result = derivative_x(1,10**-i)
	print("Derivative with delta=10^"+str(-i)+" with x = 1: "+str(result))

# In this case the accuracy is improved up to 10^-8, after that it gets worse