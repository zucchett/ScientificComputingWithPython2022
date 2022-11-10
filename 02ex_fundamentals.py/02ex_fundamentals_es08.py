# 8. The Fibonacci sequence (part 2)

# Calculate the first 20 numbers of the [Fibonacci sequence]
# (https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.

def rec_fib(n):
    if n <= 1:
        return n
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)


sequence = []
for i in range(20):
    sequence.append(rec_fib(i))
    print(sequence)
