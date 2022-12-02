import numpy as np
import math

def prime_numbers(N):
    mask = np.ones(N+1, dtype=bool)
    mask[0] = False
    mask[1] = False
    for i in range(2,int(math.sqrt(N))+1):
        if mask[i]:
            for j in range(i**2, N+1, i):
                mask[j] = False
    
    numbers = np.arange(N+1)
    primes = numbers[mask]
    return primes
            
print(prime_numbers(1000))

%timeit prime_numbers(100)
%timeit prime_numbers(1000)
%timeit prime_numbers(10000)

# As it is shown, as N grows, time it takes to calculate prime numbers grows hugely.
# And it was quite expectable, becuase of iteration.