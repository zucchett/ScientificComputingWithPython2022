# Integral of a semicircle
import math
import timeit
from cmath import phase

def semicircleArea(x): 
    return (1-pow(x,2)) ** (1/2)

def integration(f, low, up, N):
    summation = 0
    h = (up - low) / N 
    for i in range(N):
        summation = summation + h*f(i)
    return phase(summation)

print("\nExercise 7a)")

N = 100
print("Integral with N = 100: "+str(integration(semicircleArea, -1, 1, N)))
print("Real result of the integral: "+str(math.pi/2))
print("Difference between the two results: ", math.pi/2 - integration(semicircleArea, -1, 1, N))


print("\nExercise 7b)")

a = timeit.timeit(stmt='integration(semicircleArea, -1, 1, N)', globals=globals(), number=1)
while a<1:
    print("Integral with N = "+str(N)+" computed in time "+str(a))
    N = N+100000
    a = timeit.timeit(stmt='integration(semicircleArea, -1, 1, N)', globals=globals(), number=1)

N = N-100000

print("\nTo run in less than a second N can be increased to: "+str(N)+", and in this case the integral result is: "+str(integration(semicircleArea, -1, 1, N)))
print("Real result of the integral: "+str(math.pi/2))
print("Difference between the two results: ", math.pi/2 - integration(semicircleArea, -1, 1, N))

# Running the code for 1 minute would get a very high N.
# But already a 1-second computation allows a good accuracy of the integral calculation,
# consequently an accurate result can be obtained with a much lower computation time than 60 seconds
# and therefore with a lower value of N.