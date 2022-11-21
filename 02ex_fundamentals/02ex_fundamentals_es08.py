def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
l = [fib(i) for i in range(22)]
print(l)