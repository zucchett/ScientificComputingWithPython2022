import numpy as np
import timeit 
def extract_primes(n):
    mask = np.full((1,n), True)
    print(np.shape(mask))
    mask[0,0] = False
    numbers = np.arange(1,n+1)
    numbers = np.reshape(numbers,(1,n))
    print(np.shape(numbers))
    x = 2

    while x * 2 < 99:
        if x *2 <= 99:
            mask[0, (x * 2)-1] = False
        if x*3 <=  99:
            mask[0, (x *3)-1] = False
        if x * 5 <=99:
            mask[0, (x*5)-1] = False
        if x *7 <= 99:
            mask[0, (x * 7)-1] = False
        x = x+1
    print("This s the mask:\n", mask, '\n')
    print("This is matrix of prime numbers created by mask:\n", numbers[mask])
n = 120    
t = timeit.timeit('extract_primes(n)', number = 1, globals = globals())
print(t)
