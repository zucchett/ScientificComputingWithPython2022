# The derivative

def f(x):
	return x*(x-1)
    
delta=0.01
derivative = (f(1+delta)-f(1))/delta

print(derivative)