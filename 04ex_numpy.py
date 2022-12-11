import numpy as np   # import naming convention
import numpy.random as npr
from numpy import newaxis
import math
import matplotlib.pyplot as plt
from math import pow, ceil
import timeit
import pylab
# Exercise 1 - Reductions
print("Exercise 1")
m = np.arange(12).reshape((3, 4))  # matrix
print("Overall:", m.mean())  # mean of the matrix
print("Row: ", m.mean(1))  # mean of each row of the matrix
print("Column: ", m.mean(0))  # mean of each column of the matrix

# Exercise 2 - Outer product
print("\n Exercise 2")
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
print(u)
print(v)
print("The outer product using outer in numpy:")
print(np.outer(u, v))  # 1 - using the function outer in numpy
print("The outer product using a list comprehension:")
print([i * j for i in u for j in v])  # 2 - using list comprehension
print("The outer product using numpy broadcasting operations:")
print(u[:, newaxis] * v)  # 3 - using numpy broadcasting operations

# Exercise 3 - Matrix masking
print("\n Exercise 3")
random = 3 * npr.random_sample((10, 6)) - 0
print("10 by 6 matrix of float random numbers, distributed between 0 and 3 according to a flat distribution: ")
print(random)
arr = np.array(random)
mask = (random < 0.3)
print("Mask: \n", mask)
random[random < 0.3] = 0
print("\n All entries smaller than 3 set to zero using a mask: ")
print(random)

# Exercise 4 - Trigonometric functions
print("\n Exercise 4")
array = np.linspace(0, 2*math.pi, num=100)
print("The linear space with 100 values between 0 and 2*pi (inclusive):\n", array)
print("\n Extracted every 10th element using the slice notation:\n", array[::10])
print("\n Reversed the array using the slice notation:\n", array[::-1])
elements = np.abs(np.sin(array)-np.cos(array)) < 0.1
print("\n Elements where the absolute difference between "
      "the sin and cos functions is smaller than 0.1:\n", array[elements])
pylab.title("Plot showing the sin and cos functions and indicate where they are close")
pylab.plot(array, np.sin(array), array, np.cos(array))
pylab.show()

# Exercise 5 -  Matrices
print("\n Exercise 5")
print("10 by 10 multiplication table:")
ns = np.arange(1, 11)
m = ns[:, None] * ns[None, :]
print(m)
print("\n The trace of the matrix: ", m.trace())
print("\n The anto-diagonal: ", np.flipud(m).diagonal())
print("\n The diagonal offset by 1 upwards: ", m.diagonal(offset=1))

# Exercise 6 -  Broadcasting
print("\n Exercise 6")
mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
distance_array = np.abs(mileposts - mileposts[:, np.newaxis])
print("\n Distances among each city:\n", distance_array)
plt.pcolor(distance_array)
plt.colorbar()
print("\n Converted from miles in: \n", distance_array/0.62137119)   # conversion_factor = 0.62137119

# Exercise 7 - Prime numbers sieve
print("\n Exercise 7")
def sieve(n):                   # compute the prime numbers
    N = [True for i in range(n+1)]
    N[1] = False
    primes = []
    for i in range(2, ceil(pow(n, 0.5))+1):
        if N[i]:
            for j in range(i*i, n+1, i):
                N[j] = False
    for i in range(2, n+1):
        if N[i]:
           primes.append(i)
    return primes

n = int(input("Enter n: \n"))
print(sieve(n))
print(timeit.timeit('sieve(n)', globals=globals(), number=99))
# Time increases when we increase N

# Exercise 8 - Diffusion using random walk
print("\nExercise 8")
from pylab import *
u = 2 * randint(0, 2, size=(1000, 200))-1
print(u)
walking_distance = u.sum(1)
print("\n", u.sum(1))   # the walking distance for each walker
walking_distances_square = np.square(walking_distance)
print("\n", walking_distances_square)   # the square of the previously-obtained array (element-wise)
mean_distance_square = []
mean = 0
for i in walking_distances_square:
    mean += i
    mean_distance_square.append(np.mean(mean))
print(mean_distance_square)
distances = np.sqrt(walking_distances_square)
m = np.arange(0, len(distances))
plt.plot(m, distances)
plt.show()






