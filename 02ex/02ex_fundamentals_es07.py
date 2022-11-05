# Decorators

def hello(func):
	def wrapper(*args,**kwargs):
		func(*args,**kwargs)
		print("Hello World!")
		return func(*args,**kwargs)
	return wrapper

@hello	
def square(x):
    return x*x
    
l = 2
print("Initial variable value: " + str(l))
print("Squaring it three times:")
for i in range(3):
	l = square(l)
	i += 1
print("Final variable value: " + str(l))
