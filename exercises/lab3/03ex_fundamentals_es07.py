# Integral of a semicircle
from math import pi
from cmath import phase
import timeit

def semicircleArea(x): 
    return (1-pow(x,2)) ** (1/2)

def integration(f, low, up, N):
    summation = 0
    h = (up - low) / N 
    for i in range(N):
        summation = summation + h*f(i)
    return phase(summation)

print("\nExercise 7a)")

N = 10
print("Integral with N = 100: "+str(integration(semicircleArea, -1, 1, N)))
print("Real result of the integral: "+str(pi/2))


print("\nExercise 7b)")

a = timeit.timeit(stmt='integration(semicircleArea, -1, 1, N)', globals=globals(), number=1)
while a<1:
    print("Integral with N = "+str(N)+" computed in time "+str(a))
    N = N+100000
    a = timeit.timeit(stmt='integration(semicircleArea, -1, 1, N)', globals=globals(), number=1)

N = N-100000

print("\nTo run in less than a second N can be increased to: "+str(N)+"\nand in this case the result is: "+str(integration(semicircleArea, -1, 1, N)))

N = N*60

a = timeit.timeit(stmt='integration(semicircleArea, -1, 1, N)', globals=globals(), number=1)
print("\nIntegral with N = "+str(N)+" computed in time "+str(a))

print("\nTo run in less than a second N can be increased to: "+str(N)+"\nand in this case the result is: "+str(integration(semicircleArea, -1, 1, N)))