import numpy as np

def integral(N):
    h = 2/N
    I = 0
    for k in range(N):
        I += math.sqrt(1-((h*((N/2)- k))**2))
    return h*I



true_I = np.pi/2
print('N=100')
print('Numerical value of I for N=100 :', integral(100))
print('Difference between numerical result and true value for N:', abs(true_I - integral(100)) )
#The result for N=100 agrees with the predicted value up to the 2nd decimal digit.

print('\nN=1000000')
x = integral(1000000)
%timeit integral(1000000)
print('Difference between numerical result and true value for N:', abs(true_I - x) )

print('\nN=10000000')
y = integral(10000000)
%timeit integral(10000000)
print('Difference between numerical result and true value for N:', abs(true_I - y) )



