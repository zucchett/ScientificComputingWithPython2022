import timeit
from math import pi
from cmath import phase


def semi_circle(x):
    return (1-(x**2))**(1/2)

def integral(N, lower_limit, upper_limit, func):
    result = 0
    h = (upper_limit - lower_limit) / N
    
    for i in range(N):
        result = result + h * func(i)
    return phase(result)

# a)

N = 100
lower_limit = -1
upper_limit = 1

print("Result of integral: ", integral(100, -1, 1, semi_circle))
print("Result of pi/2 is ", (pi/2))

#The difference between the two value is small, almost equal with slight variation

# b)

start1 = timeit.default_timer()
integral(N*12000, lower_limit, upper_limit, semi_circle)
d1 = timeit.default_timer() - start1

start2 = timeit.default_timer()
integral(N*12000*100, lower_limit, upper_limit, semi_circle)
d2 = timeit.default_timer() - start2

print("1st duration ", d1)
print("2nd duration", d2)

