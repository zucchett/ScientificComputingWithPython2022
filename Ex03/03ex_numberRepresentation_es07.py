# 7. Integral of a semicircle
import math
import timeit
def integral(N):
    I = 0
    h = 2/N
    for i in range(1,N+1):
         I += h*math.sqrt(1-(-1 + h*i)**2)
    
    print(I)

integral(100)

n = 10000
t = timeit.Timer(lambda: integral(n))

print(t.timeit(1))
