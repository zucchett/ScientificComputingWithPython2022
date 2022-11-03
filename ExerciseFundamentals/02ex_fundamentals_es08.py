"""
8. The Fibonacci sequence (part 2)
Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.
"""


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


fib_list = []
for i in range(20):
    fib_list.append(fib(i))

print(fib_list)
