from cmath import pi
import math as m
import numpy as np
import timeit
import matplotlib.pyplot as plt

def f(x):
    return (1-x**2)**0.5


def integral(N):
    steps = [ -1+((2/N)/2)*(1+2*x) for x in range(N) ]
    result = 0
    for i in steps:
        result = result +2/N*f(i)
    return result

def compute(N):
    start = timeit.default_timer()
    res = integral(N)
    time = timeit.default_timer()-start
    # comp_time = timeit.timeit(lambda: integral(N) ,number=1)
    err = (res-(pi/2))/res
    return [res,err,time]

res100 = compute(100)
print('The obtained value is: ',res100[0])
print('Relative Error: ', res100[1])
print('Execution time [s]: ', res100[2])



delay = 0
nex = 0
N = 2500000


print('COMPUTING THE N VALUE TO GET ONE SECOND OF COMPUTATION...')

while nex < 1:
    delay = nex
    N = N+100000
    out = compute(N)
    nex = out[2]

N_one_second = N-100000

res_one_sec = compute(N_one_second)
print('Max N to get close to a second: ', N_one_second)
print('Actual computation time [s]: ', res_one_sec[2])
print('The obtained value for this N is: ',res_one_sec[0])
print('Relative Error: ', res_one_sec[1])



print('COMPUTING THE N VALUE TO GET ONE MINUTE OF COMPUTATION, MAY TAKE SOME MINUTES...')


N2 = N_one_second
nex2 = 0
curr = []
prev_N = 0
while True:
    temp = compute(N2)

    print('Last execution took: ',temp[2], 'seconds')
    
    if temp[2]>60:
        break
    elif temp[2]<10:
        prev_N = N2
        N2=N2*6
    elif temp[2]<20:
        prev_N = N2
        N2=m.floor(N2*2.3)
    elif temp[2]<30:
        prev_N = N2
        N2=m.floor(N2*1.5)
    elif temp[2]<40:
        prev_N = N2
        N2=m.floor(N2*1.2)
    elif temp[2]<50:
        prev_N = N2
        N2=N2 + N_one_second*8
    else:
        prev_N = N2
        N2=N2 + N_one_second*4
    
    curr = temp


print('Max N to get close to a minute: ', prev_N)
print('The obtained value for this N is: ',curr[0])
print('Relative Error: ', curr[1])


print('By observing the relative error between the one second and the one minute computation we can see that the gain is negligible')
