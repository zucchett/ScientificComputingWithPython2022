from cmath import pi
import math as m
import numpy as np
import timeit
import matplotlib.pyplot as plt

def f(x):
    return m.sqrt(abs(1-x**2))


def integral(N):
    steps = np.arange(-1,1,2/N) + 1/N
    return sum([(2/N)*f(x) for x in steps])

def compute(N):
    res = integral(N)
    comp_time = timeit.timeit(lambda: integral(N) ,number=1)
    err = (res-(pi/2))/res
    return [res,err,comp_time]

res100 = compute(100)
print('The obtained value is: ',res100[0])
print('Relative Error: ', (res100[1]-(pi/2))/res100[1])
print('Execution time [s]: ', res100[2])



delay = 0
nex = 0
N = 2500000
while nex < 1:
    delay = nex
    N = N+100000
    nex = timeit.timeit(lambda: integral(N) ,number=1)
N_one_second = N-100000

res_one_sec = compute(N_one_second)
print('Max N to get close to a second: ', N_one_second)
print('Actual computation time [s]: ', res_one_sec[2])
print('The obtained value for this N is: ',res_one_sec[0])
print('Relative Error: ', res_one_sec[1])



res_one_min = compute(170000000) #ATTENTETION 
print('Max N to get close to a second: ', 170000000)
print('Actual computation time [s]: ', res_one_min[2])
print('The obtained value for this N is: ',res_one_min[0])
print('Relative Error: ', res_one_min[1])

N_values = []
e = []
for i in range(100,2000):
    N_values.append(i)
    r = integral(i)
    e.append((r-(pi/2))/r)


plt.plot(N_values,e)
plt.xlabel('values of N')
plt.ylabel('Relative errors')
plt.show()
print('As expected the relative error decreases as long as N increases but not in a linear way')