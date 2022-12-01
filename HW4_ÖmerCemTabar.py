"""
Author : Ömer Cem Tabar
Exercise Document 04 Solution File

This file only includes the codes that is required to solve the questions
You can also check the outputs from the notebook

"""

"""
1\. **Reductions**

Find the total mean, and the mean for each row and column of the following matrix:

```python
m = np.arange(12).reshape((3,4))
"""
import numpy as np
m = np.arange(12).reshape((3,4))
total_mean = np.mean(m)
print("Total mean of the matrix: " + str(total_mean))
firstRowMean = np.mean(m[0])
secondRowMean = np.mean(m[1])
thirdRowMean = np.mean(m[2])
firstColumn = np.mean(m[:,0])
secondColumn = np.mean(m[:,1])
thirdColumn = np.mean(m[:,2])
fourthColumn = np.mean(m[:,3])


print("Mean of the first row: " + str(firstRowMean))
print("Mean of the second row: " + str(secondRowMean))
print("Mean of the third row: " + str(thirdRowMean))
print("Mean of the first column: " + str(firstColumn))
print("Mean of the second column: " + str(secondColumn))
print("Mean of the third column: " + str(thirdColumn))
print("Mean of the fourth column: " + str(fourthColumn))

"""
2\. **Outer product**

Find the outer product of the following vectors:

```python
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
```

Use different methods to do this:

   1. Using the function `outer` in numpy
   2. Using a nested `for` loop or a list comprehension
   3. Using numpy broadcasting operations
"""
#1. Using the function outer in numpy
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
numpyOuterProduct = np.outer(u, v)
print("Outer product with the function outer in numpy:\n")
print(numpyOuterProduct,'\n')

"""
#2.a Using a a nested for loop
lst = []
for i in u:
    for j in v:
        lst.append(i*j)
nestedForLoopOuterProduct = np.array(lst).reshape(4,4)
print("Outer product with a nested for loop approach:\n")
print(nestedForLoopOuterProduct)
"""     

#2.b Using a list comprehension
listComprehensionOuterProduct = np.array([i * j for i in u for j in v]).reshape(4,4)
print("Outer product with a list comprehension approach:\n")
print(listComprehensionOuterProduct,'\n')

#3. Using numpy broadcasting operations
broadcastingOuterProduct =  u[:, np.newaxis] * v[np.newaxis, :]
print("Outer product with a numpy broadcasting operations:\n")
print(broadcastingOuterProduct)

"""
3\. **Matrix masking**

Create a 10 by 6 matrix of float random numbers, distributed between 0 and 3 according to a flat distribution.

After creating the matrix, set all entries $< 0.3$ to zero using a mask.
""" 
#If a data set has no clear peaks (i.e. the whole graph looks flat), it's called a “uniform distribution.”
#Hence uniformly ditribution can be used for random number generation
import numpy.random as npr
matrix = npr.uniform(0,3,size=(10,6))
print("Before setting all entries with mask\n")
print(matrix,"\n")
matrix[matrix < 0.3] = 0
print("After setting all entries with mask\n")
print(matrix,"\n")

"""
4\. **Trigonometric functions**

Use `np.linspace` to create an array of 100 numbers between $0$ and $2\pi$ (inclusive).

  * Extract every 10th element using the slice notation
  * Reverse the array using the slice notation
  * Extract elements where the absolute difference between the `sin` and `cos` functions evaluated for that element is $< 0.1$
  * **Optional**: make a plot showing the sin and cos functions and indicate where they are close
"""
import math as m
original_array = np.linspace(0,2*m.pi,100)
print("Original array that we have created according to the question:\n")
print(original_array,"\n")

print("After extracting the every 10th element using the slice notation we have obtained:\n")
extracted_array = original_array[9::10]
print(extracted_array,"\n")

print("After reversing the array using the slice notation of the extracted array:\n")
reverse_array = original_array[::-1]
print(reverse_array,"\n")

print("After extracting the elements according to the difference between sin and cos functions which less than 0.1:\n")
mask = np.abs(np.sin(original_array)-np.cos(original_array)) < 0.1
extracted_new = original_array[mask]
print(extracted_new,"\n")

print("Optional part for making a plot to show sin and cos functions close points\n")
import matplotlib.pyplot as plt
plt.scatter(extracted_new, np.sin(extracted_new))
plt.plot(original_array, np.sin(original_array), original_array, np.cos(original_array));
plt.xlabel('x values from 0 to 2pi')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 2pi')
plt.show()

"""
5\. **Matrices**

Create a matrix that shows the 10 by 10 multiplication table.

 * Find the trace of the matrix
 * Extract the anti-diagonal matrix (this should be ```array([10, 18, 24, 28, 30, 30, 28, 24, 18, 10])```)
 * Extract the diagonal offset by 1 upwards (this should be ```array([ 2,  6, 12, 20, 30, 42, 56, 72, 90])```)
"""
a = range(1,11) # default step value is 1, no need to specify
b = range(1,11)

multiplication_matrix = [[i*j for j in a] for i in b]
multiplication_matrix = np.array(multiplication_matrix).reshape(10,10)
print("Original multiplication matrix:\n")
print(multiplication_matrix,"\n")

print("Trace of the matrix: ",sum(multiplication_matrix.diagonal()),'\n')


print("Anti diagonal of the matrix:\n")
print(multiplication_matrix[::-1].diagonal(),"\n")

print("Diagonal of the matrix with offset 1 and upwards matrix:\n")
print(multiplication_matrix.diagonal(1),"\n")

"""
6\. **Broadcasting**

Use broadcasting to create a grid of distances.

Route 66 crosses the following cities in the US: Chicago, Springfield, Saint-Louis, Tulsa, Oklahoma City, Amarillo, Santa Fe, Albuquerque, Flagstaff, Los Angeles.

The corresponding positions in miles are: 0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448

  * Build a 2D grid of distances among each city along Route 66
  * Convert the distances in km
"""
#We are currently in Chicago.That is why the poisiton of Chicago is set to 0
#Cities =[ Chicago, Springfield, Saint-Louis, Tulsa, Oklahoma City, Amarillo, Santa Fe, Albuquerque, Flagstaff, Los Angeles]
positions = np.array([0,198,303,736,871,1175,1475,1544,1913,2442])
x = positions
y = positions[:, np.newaxis]
distances = abs(x - y)
print("Before the convertion of miles to km we have 2D distances grid as:\n")
print(distances,"\n")

distancesKM = distances * 1.609344
print("After the convertion of miles to km we have 2D distances grid as:\n")
print(distancesKM)
"""
7\. **Prime numbers sieve**

Compute the prime numbers in the 0-N (start with N=99) range with a sieve (mask).

  * Constract a shape (N,) boolean array, which is the mask
  * Identify the multiples of each number starting from 2 and set accordingly the corresponding mask element
  * Apply the mask to obtain an array of ordered prime numbers
  * Check the performances (with `timeit`); how does it scale with N?
  * Implement the optimization suggested in the [sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
"""
import math as mat
N = 99
primeNumberMask = np.array(np.arange(0,N+1),bool)
numbers = np.arange(0,N+1)

primeNumberMask[:2] = False
for beforeIndex in range(2,N+1):
    for afterIndex in range(beforeIndex+1,N+1):
        if afterIndex%beforeIndex==0 and primeNumberMask[afterIndex]== True:
            primeNumberMask[afterIndex]=False

print("Before filtering with the mask we have:\n")
print(numbers,'\n')
print("After filtering the array with the mask we obtain:\n")
filtered_numbers = numbers[primeNumberMask]

#%timeit numbers[primeNumberMask]
print(filtered_numbers,'\n')

#942 ns ± 5.67 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each) for N=99
#1.41 µs ± 8.28 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each) for N=250
#2.49 µs ± 13.5 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each) for N=500
#4.63 µs ± 18.8 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each) for N=1300

#We obtained that when N increases, time to obtain the masked array increases. For instance even between N=99 and N=250
#time to take to obtain the masked array is much more slower in N=250 than the N=99
#That is why whenever we increase the N, it will take more time to obtain the prime number array with masking
#if we are not approachin the calculation with sieve approach
def SieveOfEratosthenes(N):
    #Set all the list as True for N numbers with list comprehension 
    primeNumbersBoolean = [True for i in range(N+1)]
    primeNumbers = []
    number = 2
    while (number <= int(np.sqrt(N))):
        if (primeNumbersBoolean[number] == True):
            for index in range(number * number, N+1, number):
                primeNumbersBoolean[index] = False
        number += 1
  
    # Return all prime numbers
    for number in range(2, N+1):
        if primeNumbersBoolean[number]:
            primeNumbers.append(number)
    return primeNumbers
    
PrimeNumbersFromSieveOfErasthothenes = SieveOfEratosthenes(N)
print("After the process of sieve of erasthothenes we obtained the prime numbers as: \n")
print(np.array(PrimeNumbersFromSieveOfErasthothenes))

"""
8\. **Diffusion using random walk**

Consider a simple random walk process: at each step in time, a walker jumps right or left (+1 or -1) with equal probability. The goal is to find the typical distance from the origin of many random walkers after a given amount of time.

*Hint*: create a 2D array where each row represents a walker, and each column represents a time step.

  * Take 1000 walkers and let them walk for 200 steps
  * Use `randint` to create a 2D array of size $walkers \times steps$ with values -1 or 1
  * Calculate the walking distances for each walker (e.g. by summing the elements in each row)
  * Take the square of the previously-obtained array (element-wise)
  * Compute the mean of the squared distances at each step (i.e. the mean along the columns)
  * **Optional**: plot the average distances ($\sqrt(distance^2)$) as a function of time (step)
"""
import matplotlib.pyplot as plt
import numpy.random as npr
import math as mat
import warnings


    

#Using randint we obtained a matrix which consists of -1,0,1
#After the multiplication of 2 and substution with 1 gives us a matrix with -1 and 1
walkersAndSteps = npr.randint(0,2,(1000,200)) * 2 - 1
print("Walkers and Steps matrix:\n")
print(walkersAndSteps , '\n')

#In order to calculate the last locations of the each walker after 200 steps
#We can also obtain the total sum in each row
endingWalkers = walkersAndSteps[:,199]
#print(endingWalkers)

#But for the question we have to calculate the cumuvalitve sum in each row
#Since we know that question seeks for the mean square distance for 1000 walkers in each time step
#walkersAndSteps = np.cumsum(walkersAndSteps,axis=1)
for row in range(0,len(walkersAndSteps)):
    for col in range(0,len(walkersAndSteps[row])):
        walkersAndSteps[row,col] = walkersAndSteps[row,col-1] + walkersAndSteps[row,col]
print("After we have cumulatively sum the walkin distances of each walker:\n")
print(walkersAndSteps,'\n')

#Squared distances of walkers in each time step (obtained by element wised sqaure operation)
#Being left or right does not important from now on
#We are seeking how far the walkers from starting point in each time step
squaredwalkersAndSteps = np.square(walkersAndSteps)
print("Square of the walking distances:\n")
print(squaredwalkersAndSteps,'\n')
meanAlongColumns = []
for i in range(0,200):
    meanAlongColumns.append(np.mean(squaredwalkersAndSteps[:,i]))
    
meanAlongColumnsNP = np.array(meanAlongColumns)
#print(meanAlongColumnsNP)
print("Mean of the squared distances at each step(mean along the columns):\n")
print(meanAlongColumnsNP)

############## OPTIONAL #################

plt.plot(meanAlongColumnsNP)
plt.xlabel('Time step')
plt.ylabel('Mean Squared Distances')
plt.title('Mean Squared Distances At Each Time Step')
plt.show()







