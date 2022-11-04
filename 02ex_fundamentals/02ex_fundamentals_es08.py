"""8. The Fibonacci sequence (part 2)
Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.
"""

fibo_seq = []


def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        b = fibo(n-2)+fibo(n-1)
        return b

for i in range(1,21):
    fibo_seq.append(fibo(i))

print(fibo_seq)


