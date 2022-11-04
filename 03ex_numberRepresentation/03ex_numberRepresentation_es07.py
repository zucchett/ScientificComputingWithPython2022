import math
import timeit
import numpy as np

def func(x):
    return math.sqrt(1 - x**2)

def calculate_area(delta):
    s = 0
    for x in np.arange(-1,1,delta):
        s += func(x) * delta
    return s



n = 100
delta = 2/n
area = calculate_area(delta)
print("This is the area for N=100: ", area)

t = 0
while t < 1:
    delta = 2/n
    t = timeit.timeit(lambda: calculate_area(delta), number = 1)
    last_n = n
    n *= 2
    print("This is n: ", n)
    print("This is t: ", t)
print("This is the maximum n for caculating the area in less than a minute: ", last_n)
print('______________________________')
