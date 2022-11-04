'''
Fibonacci sequence using a recursive function
'''
import timeit

def recursiveFibonacci(n):
    if n<2:
        return 1
    else:
        return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

start = timeit.default_timer()
recursiveFibonacci(20)
exe_time = timeit.default_timer() - start
print("Fibonacci sequence using a recursive function execution time:", exe_time)


