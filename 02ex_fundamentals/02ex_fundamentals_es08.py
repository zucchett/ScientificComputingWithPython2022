def recursiveFib(x):
    if x==1 or x==0:
        return 1
    else:
        return recursiveFib(x-2) + recursiveFib(x-1)

fib = []   
for i in range(20):
    fib.append(recursiveFib(i))
    
print("The first", len(fib), "numbers of the Fibonacci sequence are: \n", fib)
print()
