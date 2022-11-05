import timeit
#implementazione for e while

def recfib(n):
        if n<=1:
                return n
        else:
                return (recfib(n-1)+recfib(n-2))
def itfib(n):
	xn=1
	xm=1	
	i=0
	while i<n-2:
        	xp=xn+xm
        	xm=xn
        	xn=xp
        	i=i+1
#%timeit recfib(20)
#%timeit recfib(20)
print("recursive fibonacci: 11 ms ± 140 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)")
print("iterative fibonacci: 9.37 µs ± 288 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)")
#the iterative fibonacci takes less time and computational effort as it stores in the memory the values of the 
#fibonacci numbers calculated up until that point
#Insthead the recursive fibonacci needs to repeat the entire procedure for smaller instances every time the function 
#is called, this leads to a huge amount of operations as n gets bigger
