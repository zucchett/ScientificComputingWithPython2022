"""
11. The Fibonacci sequence

Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number)
using only `for` or `while` loops.
"""

fibonacci = [0]

n1 = 0
n2 = n1 + 1

for i in range(19):
    fib = n1 + n2
    fibonacci.append(fib)
    n1 = n2
    n2 = fib

print("The first 20 numbers of the Fibonacci sequence are: \n", fibonacci)
