#Integral of a semicircle

from math import sqrt

print('######### (a) #########')

def Riemann(N):
    I = 0
    h = 2/N
    for k in range(1,N+1):
        x = -1 + k*h      #change of variable
        y_k = sqrt(1-x**2)
        I += y_k
    I *= h
    return I

print('calculation of the integral using Riemann definition:',Riemann(100))

# the result is too close to the real value and if we keep on increasing N it will be closer

print('######### (b) #########')
import timeit
N=100
while(True):
    start=timeit.default_timer()
    Riemann(N)	
    end=timeit.default_timer()
    time= abs(end-start)
    if(time>=1):
        break
    elif(time >0 and time <0.90):
        N*=2
    else:
        N+=1
    

print(N,Riemann(N))

#if we run the calculation for 1 minute we will find N =209715200 and Riemann(N) = 1.570796326794599
#so the more we increase N we converge to the real value og the integral


