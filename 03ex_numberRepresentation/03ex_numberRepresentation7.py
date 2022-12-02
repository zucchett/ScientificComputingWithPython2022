# 7. Integral of a semicircle
from math import sqrt

# point a

N = 100

def f(N):
    h = 2/N
    integral = 0
    for i in range(N):
        xk = -1 + h*i
        yk = sqrt(1 - xk**2)
        integral += yk*h
    return integral

print(f(N))

# With N = 100 we obtain 1.5691342555492505 estimation 
# of pi/2 with a precision of 10^(-1)



# point b

import timeit

N = 4000000
time = 0
lasttime = 0.4

while (lasttime - time) < 1:
    time = timeit.default_timer()
    f(N)
    lasttime = timeit.default_timer()
    print(lasttime-time)
    N += 100000

print(N)    #6000000      
print(f(N)) #1.570796326681797 get an estimation of pi/2 with a precision of 10^(-9)