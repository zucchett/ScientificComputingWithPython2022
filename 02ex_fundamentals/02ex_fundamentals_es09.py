"""9. The Fibonacci sequence (part 3)
Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci
function from 01ex that use only for and while loops.
Measure the execution code of the two functions with timeit (link to the doc), for example:
%timeit loopFibonacci(20)
%timeit recursiveFibonacci(20)
which one is the most efficient implementation? By how much?
"""
import timeit


def first_solve(n=20):
    i = 0
    a, b = 0, 1
    finona = []
    while i < n:
        i += 1
        finona.append(b)
        a, b = b, a + b
    return finona


def second_solve(n):
    if n == 1 or n == 2:
        return 1
    else:
        return second_solve(n-2)+second_solve(n-1)


first_time = timeit.Timer(lambda: first_solve(20))
second_time = timeit.Timer(lambda: second_solve(20))
#
print(first_time.timeit(1))
print(second_time.timeit(1))

# print(timeit.timeit(first_solve(20)))
