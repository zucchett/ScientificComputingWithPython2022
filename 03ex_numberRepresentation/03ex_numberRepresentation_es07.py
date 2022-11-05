import math

def circle(x):
	return math.sqrt(1-(x**2))

def integral(N):
	y=[]
	h=2/N
	k=-1
	i=0
	while i<N:
		y.append(circle(k))
		k+=h
		i+=1
	sum=0
	for i in range(N):
		sum=sum+h*y[i]
	return sum
print("The result of the integral for N=100 is:")
print(integral(100))
#%timeit integral(300000)
print("FOR N=100: 303 µs ± 22.8 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)")
print("FOR N=300000: 997 ms ± 33.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)")
#as N increases, also the computation time increases, and the output of the algorithm gets closer to the real value
