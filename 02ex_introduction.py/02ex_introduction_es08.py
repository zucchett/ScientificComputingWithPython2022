def fib(f):
    if f < 2:
        return 1
    return fib(f-1) + fib(f-2)
print([fib(i) for i in range(20)])

