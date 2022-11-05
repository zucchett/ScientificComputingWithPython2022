# The Fibonacci Sequence

n = 20

if n == 0:
	fib = []
elif n == 1:
	fib = [0]
else:
	fib = [0,1]
	while len(fib) < n:
		fib.append(fib[len(fib)-1]+fib[len(fib)-2])
print(fib)
