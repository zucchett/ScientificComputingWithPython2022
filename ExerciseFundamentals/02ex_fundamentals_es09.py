"""
9.The Fibonacci sequence (part 3)
Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use
only for and while loops.
Measure the execution code of the two functions with timeit (link to the doc), for example:
%timeit loopFibonacci(20)
%timeit recursiveFibonacci(20)
which one is the most efficient implementation? By how much?
"""

import timeit


def recursiveFibonacci(n):
    if n == 0 or n == 1:
        return n
    return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)


def loopFibonacci(n):
    f = [1, 1]
    i = 2
    while i <= n:
        f.append(f[i - 1] + f[i - 2])
        i = i + 1
    return f


starttime_loop = timeit.default_timer()
loopFibonacci(20)
TimeEnd_loop = timeit.default_timer() - starttime_loop
print("Execution time for loopFibonacci :", TimeEnd_loop)
starttime_rec = timeit.default_timer()
recursiveFibonacci(20)
TimeEnd_rec = timeit.default_timer() - starttime_rec
print("Execution time for recursiveFibonacci :", TimeEnd_rec)
print("loopFibonacci is more efficient than recursiveFibonacci, it is", (TimeEnd_rec / TimeEnd_loop), "times faster.")
