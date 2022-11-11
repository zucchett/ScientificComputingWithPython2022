"""
7. Prime numbers sieve
Compute the prime numbers in the 0-N (start with N=99) range with a sieve (mask).
Constract a shape (N,) boolean array, which is the mask
Identify the multiples of each number starting from 2 and set accordingly the corresponding mask element
Apply the mask to obtain an array of ordered prime numbers
Check the performances (with timeit); how does it scale with N?
Implement the optimization suggested in the sieve of Eratosthenes
"""
import numpy as np
import timeit
N=100
a = np.arange(1, N)
primes = np.array([])

for i in a:
    mask1 = (a<=i)
    filtered_a = a[mask1]                       #mask1 (numbers < i)
    mask2 = (i%filtered_a==0)
    dividers = filtered_a[mask2]              #mask2 (list of dividers of i)
    if dividers.size == 2:
        primes = np.append(primes, i)          #list of prime numbers (divided just by 1 and themselfs)
print("List of prime numbers in range 0 -",N,":  \n\n", primes.astype(int))