#9. The Fibonacci sequence (part 3)

def Fibonacci_rec(n):
    """Fibonacci_rec is recursive"""
    if n==0: 
        return 0
    elif n==1: 
        return 1
    else:
        return Fibonacci_rec(n-1)+Fibonacci_rec(n-2)
    
def Fibonacci_iter(n):
    """Fibonacci_iter is iterative"""
    x,y = 0,1
    for i in range(n):
        x,y = y,x+y
    return x
import timeit
%timeit Fibonacci_rec(20) #3.29 ms ± 48.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) ==> 329 ms in general
%timeit Fibonacci_iter(20)#1.43 µs ± 12 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)==> 143 ms in general

#The iterative method is more efficient by approximativaly 186 ms and also memory efficient as we store only the last two values. 
