# The Fibonacci Sequence (part 3)

import timeit as t

def loopfibonacci(n):
	if n == 0:
		fib = []
	elif n == 1:
		fib = [0]
	else:
		fib = [0,1]
		while len(fib) < n:
			fib.append(fib[len(fib)-1]+fib[len(fib)-2])
	return fib

def recursivefibonacci(w):
	def fibonacci(x):
		if x-int(x) == 0:
			if x == 0 or x == 1:
				return 0
			elif x == 2:
				return 1
			else:
				return fibonacci(x-1)+fibonacci(x-2)
	l = []	
	for i in range(w):
		l.append(fibonacci(i+1))
	return l

# I know that I would fix the integer 20 as the argument for the two functions, so I did not make extra checks if they really are integers

lofi = format(t.timeit(lambda: loopfibonacci(20), number = 1), ".10f")
refi = format(t.timeit(lambda: recursivefibonacci(20), number = 1), ".10f")

print("Loop Fibonacci execution time: " + str(lofi) + " seconds.")
print("Recursive Fibonacci execution time: " + str(refi) + " seconds.")

if (lofi < refi):
	print("Loop Fibonacci calculation is faster.")
elif (refi < lofi):
	print("Recursive Fibonacci calculation is faster.")
else:
	print("How is this possible")
