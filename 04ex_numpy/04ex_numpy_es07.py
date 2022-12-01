#7. Prime numbers sieve

import numpy as np
import timeit
starting_time=timeit.default_timer()
N=100
a=np.full((N,),True)
a[0],a[1]=False,False
for i in range(2,N):
    for j in range(i+1,N):
        if j%i==0 and a[j]== True:
            a[j]=False

b=np.arange(N)
print('The prime numbers between 0 and 100:\n',b[a])
print("First time difference :", timeit.default_timer() - starting_time,'\n')

starting_time=timeit.default_timer()
a=np.full((N,),True)
a[0],a[1]=False,False

for i in range(2,N):
    for j in range(i**2,N,i):
        if j%i==0 and a[j]== True:
            a[j]=False

b=np.arange(N)
print('The prime numbers between 0 and 100:\n',b[a])
print("Second time difference for the optimized algorithm:", timeit.default_timer() - starting_time)

#The second time diffrence is lower than the first one and that's because the second method is optimized.
