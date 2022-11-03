fib= [0, 1]
def loopFibonacci(n):
    for i in range(2, n):
        fib.append(fib[i-1]+fib[i-2])
        
        
'''
%timeit 3.25 µs ± 305 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

using for loop is more time consuming
'''
