import timeit

def loop_fib(n):
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[i-2] + fib[i-1])
    return fib

def recursive_fib(n):
    if n == 0 or n == 1:
        return n 
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

loopy = timeit.timeit(lambda: loop_fib(20), number = 1)
rec = timeit.timeit(lambda: recursive_fib(20), number = 1)

print('Loop: ', loopy)
print('Recursive: ', rec)

#Since the time taken by recursive function is far less than the method using loop, it is understood that recursive way is most efficient one.
