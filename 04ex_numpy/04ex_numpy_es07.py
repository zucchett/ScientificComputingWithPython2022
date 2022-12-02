import numpy as np
import timeit 

def generate_prime(n):
    # Initial a mask with all True values
    msk = np.full((n + 1), True)

    # Set mask to False in non-desired locations
    for i in range(2, int(np.sqrt(n)) + 1):
        if not msk[i]:
            continue
        for j in range(i**2, n + 1, i):
            msk[j] = False

    # Create a full spectrum of integer numbers within the input range
    nums = range(n + 1)
    # Return portion of numbers where mask is true
    return np.array(nums)[msk]



n = 100
print(generate_prime(n))
t = timeit.timeit('generate_prime(n)', number = 1, globals = globals())
print(t)
