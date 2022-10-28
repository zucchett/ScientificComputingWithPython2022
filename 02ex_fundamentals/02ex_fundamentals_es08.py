def Fib(i):
    if i<=1:
        return i
    else:
        return Fib(i-2)+Fib(i-1)

print(list(map(Fib, range(20))))