fib = [0, 1]

for i in range(2,20):
    fib.append(fib[i-2] + fib[i-1])
    
print("The first 20 numbers of the Fibonacci sequence: ",fib)
