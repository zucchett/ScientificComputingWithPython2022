# The Fibonacci Sequence


def fib(n):
    f = [1,1]
    i = 2
    while i <= n:
        f.append(f[i - 1] + f[i - 2])
        i = i + 1
    return f

print(str(fib(19)))

