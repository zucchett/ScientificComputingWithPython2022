fib = []

def recurcive_fib(x):
    if x == 1 or x == 0:
        return x
    return recurcive_fib(x-1) + recurcive_fib(x-2)
        
for i in range(20):
    fib.append(recurcive_fib(i))
    
print(fib)
