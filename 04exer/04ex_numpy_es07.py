#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import numpy as np
import math as m
#sieve of Eratosthenes
"""    Returns a list of all primes < maxp.
"""
"""
def primes(maxp):
    sieve = [True for x in range(maxp)]
    prime_lst = [1]
    for i in range(2, int(m.sqrt(maxp))):
        if sieve[i]:
            prime_lst.append(i)
            for j in range(2*i, maxp, i):
                sieve[j] = False
    return prime_lst
"""
n=100
Primes=[True for k in range(n+1)]
print(Primes)
p=2
Primes[1]=False
Primes[0]=False
while(p*p<=n):
    if Primes[p]==True:
        for j in range(p*p,n+1,p):
            Primes[j]=False
    p+=1

for i in range(2,n):
   if Primes[i]:
        print(i,end=' ')


           
def prime_eratosthenes(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print (i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)

print(prime_eratosthenes(100))



