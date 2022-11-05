#7. Integral of a semicircle

#a
import numpy as np
from math import sqrt
N=100
xk=np.linspace(-1, 1,num=N)
s=0
for i in range(1,N+1):
    s+=(2/N)* sqrt(1-xk[i-1]**2)
print("The computed integral of the semicircle for N=100 is:",s)
#The result is 1.5534179294048955 which is close to the true value(1.57079632679..)


#b
import timeit
t=0
while t<1:
    start_time=timeit.default_timer()
    N*=10
    xk=np.linspace(-1, 1,num=N)
    s=0
    for i in range(1,N+1):
        s+=(2/N)*sqrt(1-xk[i-1]**2)
    t=timeit.default_timer()-start_time
print("N can be increased to:%d without surpassing 1 second of code running"%N)
print("The computed integral of the semicircle for N=%d is: %.11f"%(N,s))
# N can be increased to 10000000
#The result is more close to the real value than for just 100 iteration

#If the code is running for a whole minute that means that N is so big
#Actually, if N is so big we get to slice the interval [-1,1] to many small intervals giving more information about the function 

#Hence, we get a more precised result that is very close to the real value 
