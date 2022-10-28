# The Fibonacci Sequence (part 2)

def fibonacci(x):
	if x-int(x) == 0:
		if x == 0 or x == 1:
			return 0
		elif x == 2:
			return 1
		else:
			return fibonacci(x-1)+fibonacci(x-2)

l = []	
for i in range(20):
	l.append(fibonacci(i+1))
print(l)
