# fibonacci sequence with first 20 numbers  F_{n}=F_{n-1}+F_{n-2}}

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib_seq(x):
    sequence = []
    for i in range(0, x):
        sequence.append(fibonacci(i))
    return sequence


print(fib_seq(20))
