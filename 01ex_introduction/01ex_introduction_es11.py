fib = [0 for i in range(22)] 
fib[1] = 1
for i in range(2,len(fib)):
    fib[i] = fib[i-1] + fib[i-2]
print(fib)