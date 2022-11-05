# 7. Prime numbers sieve

# Compute the prime numbers in the 0-N (start with N=99) range with a sieve (mask).

# Constract a shape (N,) boolean array, which is the mask
# Identify the multiples of each number starting from 2 and set accordingly the corresponding mask element
# Apply the mask to obtain an array of ordered prime numbers
# Check the performances (with timeit); how does it scale with N?
# Implement the optimization suggested in the sieve of Eratosthenes

# -------------------------------------- Code Begin-------------------------------------
import numpy as np, timeit

N = 99

def prime(N):
    mask = np.ones(N+1,  dtype=bool)
    for p in range(2,N+1):
        mask[p+1:N+1] *= np.invert((np.arange(p+1, N+1) % p == 0))
    return np.where(mask)


def sieveOfEratosthenes(N):
    mask = np.ones(N+1,  dtype=bool)
    p=2
    while(p*p <=N):
        mask[p+1:N+1] *= np.invert((np.arange(p+1, N+1) % p == 0))
        p +=1
    return np.where(mask)

    

print("the prime numbers in the 0-N range with a sieve (mask) : \n ", prime(N))
print('\n ------------------------------------------- \n')

print("the prime numbers in the 0-N with optimization suggested in the sieve of Eratosthenes : \n ", sieveOfEratosthenes(N))
print('\n ------------------------------------------- \n')

for i in range(100,1000,100):
    start=timeit.default_timer()
    sieveOfEratosthenes(i)
    end=timeit.default_timer()
    print('The execution time for N = ',i,' is : ',end-start)

# The more N increase the more the execution time
    

# -------------------------------------- Code End---------------------------------------
