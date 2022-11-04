fib= [0, 1]

for i in range(18):
    fib.append(fib[i]+fib[i+1])
    
print(' the first 20 numbers of the Fibonacci sequence:', fib)
