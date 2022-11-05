# 7. Integral of a semicircle
import math
import timeit

trueValue = 1.57079632679 # From the Jupyter notebook

def integral(N):
    I = 0
    h = 2/N
    for i in range(1,N+1):
         I += h*math.sqrt(1-(-1 + h*i)**2)
    print('\nTrue Value:',trueValue)
    print('Integral Value for N = %d:'%N,I)
    print('Difference between True value and Integral Value:', (trueValue - I))
    print('Accuracy:',100 - ((trueValue - I)*100/trueValue))

print('Time for N=100:',timeit.timeit(lambda: integral(100), number=1))

n = 4353630
t = timeit.timeit(lambda: integral(n), number=1)
print('Time for N = 4353630:',t)

# The Integral value for N = 100 is less accurate when compared to higher N and is of by around 0.0016620712407495741
# Whereas the Integral value for N = 4353630 is quite accurate is of by around 1.7824230980068023e-10
# The gain that I could observe for running this computation for 1 sec is that we get 99.999 % Accuracy. I don't see any gain in running it for 1 minute.

'''
Used this to find the value of n, that would lead to over 1 sec of run-time.
while True:
    n+=2
    t = timeit.timeit(lambda: integral(n), number=1)
    if(t<1.0):
        print(t)
    else:
        break
'''







