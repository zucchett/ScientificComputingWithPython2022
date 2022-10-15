# The Fibonacci Sequence

fib = [0,1]

print(len(fib))

while len(fib) < 20:
	fib.append(fib[len(fib)-1]+fib[len(fib)-2])

print(fib)
