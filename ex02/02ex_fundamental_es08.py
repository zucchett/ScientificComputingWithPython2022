def fibo(n):
    if n < 2:
        return 1
    return fibo(n-1) + fibo(n-2)
print([fibo(i) for i in range(20)])