def fib_rec(n):
    if n<=1:
        return n
    else:
        return fib_rec(n-1)+fib_rec(n-2)


def fibonacci(n):
    fib = []
    for i in range(n+1):
        if i == 0 or i == 1:
            fib.append(i)
        else :
            fib.append(fib[i-1]+fib[i-2])
    return fib[n]

#%timeit fibonacci(20)
#%timeit fib_rec(20)

#3.85 µs ± 131 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
#2.14 ms ± 17.4 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)


#the loop fibonacci is more efficient than the recursive by 2,136 ms