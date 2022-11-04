import math
from timeit import timeit

# The function Riemann1 can return unprecise values when N increases a lot 
"""
def Riemann1(N):
    somma = 0
    k = -1
    while k<1 :
        somma = somma + math.sqrt(1-k**2)
        k = k+2/N
    integral = 2*somma/N
    return integral
"""

def Riemann(N):
    somma = 0
    k = -1*N
    while k<N :
        somma = somma + math.sqrt(N**2-k**2)
        k = k+2
    integral = 2*somma/N**2
    return integral

I = math.pi/2

I100 =  Riemann(100)

print("The integral of a semicircle of radius 1 is: ", I)
print()
print("The integral obtained with the Riemman formula and N=100 is: ", I100)


time100 = timeit(stmt = 'Riemann(100)', setup = 'import math', number = 1, globals=globals())

print("The time employed with N = 100 is: ", time100, "seconds")
print("The relative error between the real value of the integral and the value calculated with N = 100 is: ", (I - I100)/I)
print()

n = 2*10**6
I_n = Riemann(n)

time_n = timeit(stmt = 'Riemann(n)', setup = 'import math', number = 1, globals=globals())

print("With N =", n, "the time employed is: ", '%.2f' % time_n, "seconds and the result obtained is: ", I_n)
print("In this case the relative error is: ", (I - I_n)/I)
print()


m = 9*10**7
I_m = Riemann(m)

time_m = timeit(stmt = 'Riemann(m)', setup = 'import math', number = 1, globals=globals())

print("With N =", m, "the time employed is: ", '%.2f' % time_m, "seconds and the result obtained is: ", I_m)
print("In this case the relative error is: ", abs(I - I_m)/I)

# Using the Riemann equation but modified to work on an interval (-N, N) the accuracy between the real value of the 
# integral and the calculated value increases with increasing values of N. 
# This modification is needed because in this way the quantity added to k at each iteration is alway equal to two instead of deminishing for increasing N

