#Fibonacci Sequence

def Fib(n):
    if n <= 1:
        return n
    else:
        return Fib(n - 1) + Fib(n - 2)

def Fib_seq(x):
    seq = []
    for i in range(0, x):
        seq.append(Fib(i))
    return seq
#printing first 20 numbers
print(Fib_seq(20))


