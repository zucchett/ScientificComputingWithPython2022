fib=[0,1]
n=20
for i in range(n-2):
    fib.append(fib[i] + fib[i+1])
print(fib)