# The Fibonacci sequence (part 3)

# Run both the Fibonacci recursive function from the previous exercise, and the
# Fibonacci function from 01ex that use only for and while loops.
# Measure the execution code of the two functions with timeit (link to the doc), for example:
# %timeit loopFibonacci(20)
# %timeit recursiveFibonacci(20)
# which one is the most efficient implementation? By how much?

import timeit


def rec_fib(n):
    if n == 0 or n == 1:
        return n
    return rec_fib(n - 1) + rec_fib(n - 2)


def loop_fib(n):
    f = [1, 1]
    i = 2
    while i <= n:
        f.append(f[i - 1] + f[i - 2])
        i = i + 1
    return f


time_rec_fib = timeit.Timer(lambda: rec_fib(20))
time_loop_fib = timeit.Timer(lambda: loop_fib(20))
print("Execution time for recursive fibonacci :")
print(time_rec_fib.timeit(20))
print("Execution time for loop fibonacci :")
print(time_loop_fib.timeit(20))
