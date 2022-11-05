from math import sqrt
import timeit
n= 100

def f(n):
    h = 2/n
    integral = 0
    for i in range(n):
        xk = -1 + h*i
        yk = sqrt(1 - xk**2)
        integral += yk*h
    return integral

print(f(n))


n = 4000000
time = 0
lasttime = 0.4

while (lasttime - time) < 1:
    time = timeit.default_timer()
    f(n)
    lasttime = timeit.default_timer()
    print(lasttime-time)
    n += 100000

print(n)    
print(f(n))