
"""
Created on Mon Oct 31 16:46:57 2022

@author: Ruben
"""
import math
import timeit

N=100
I=0
h=2/N
import math
def f(x):
    return math.sqrt(1-x**2)
for i in range(N+1):
    I += f(-1+i*h)*h
print("\nRelative error with respect to the true value of pi")
print(abs(math.pi/2-I)/math.pi)

#For N=100 a relative error of 5*10**-4 is obtained

t=timeit.timeit(stmt='''
for i in range(N+1):
    I += f(-1+i*h)*h''', 
                setup='''
N=4*10**6
I=0
h=2/N
import math
def f(x):
    return math.sqrt(1-x**2)''', 
                number=1)
print("\nTime elapsed:")
print(t)

#For N=4*10**6 the computation runs for less than a second 

N_sec=4*10**6
I_sec=0
h=2/N_sec
for i in range(N_sec+1):
    I_sec += f(-1+i*h)*h

N_min=N_sec*60
I_min=0
h=2/N_min
for i in range(N_min+1):
    I_min += f(-1+i*h)*h

print("\nGAIN:")
print(abs(I_min-I_sec))

#Running the code for a minute a gain of the  of 10**-10 is obtained