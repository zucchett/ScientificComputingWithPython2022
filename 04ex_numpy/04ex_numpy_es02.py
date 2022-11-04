# 2. Outer product

# Find the outer product of the following vectors:

# u = np.array([1, 3, 5, 7])
# v = np.array([2, 4, 6, 8])
# Use different methods to do this:

# Using the function outer in numpy
# Using a nested for loop or a list comprehension
# Using numpy broadcasting operations

# -------------------------------------- Code Begin-------------------------------------
import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
w = np.array([i*j for i in u for j in v]).reshape((len(u),len(v)))

print('The outer product of u & v using outer function : \n', np.outer(u,v))
print('The outer product of u & v using list comprehension : \n', w)
print('The outer product of u & v Using numpy broadcasting operations : \n', v*u[:,None])


# -------------------------------------- Code End---------------------------------------
