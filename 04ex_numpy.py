##Anaïs FRAGNE
#Lab4: NUMPY
#1. Reductions
import  numpy as np 
#Find the total mean, and the mean for each row and column of the following matrix:

m = np.arange(12).reshape((3,4))
print('total mean is: ',np.mean(m))
print('mean of the columns: ',np.mean(m,axis=0))
print('mean of the lines: ',np.mean(m,axis=1))
 
#2. Outer product

#Find the outer product of the following vectors:

u = np.array([1, 3, 5, 7])
print(u)
v = np.array([2, 4, 6, 8])
print(v)
#Use different methods to do this:

#Using the function outer in numpy
print('Outer product: ',np.dot(u,v))
#Using a nested for loop or a list comprehension
#Using numpy broadcasting operations
 
#3. Matrix masking

#Create a 10 by 6 matrix of float random numbers, distributed between 0 and 3 according to a flat distribution.

#After creating the matrix, set all entries <0.3 to zero using a mask.


 
#4. Trigonometric functions

#Use np.linspace to create an array of 100 numbers between 0 and 2π (inclusive).

#Extract every 10th element using the slice notation
#Reverse the array using the slice notation
#Extract elements where the absolute difference between the sin and cos functions evaluated for that element is <0.1
#Optional: make a plot showing the sin and cos functions and indicate where they are close

 
#5. Matrices

#Create a matrix that shows the 10 by 10 multiplication table.

#Find the trace of the matrix
#Extract the anti-diagonal matrix (this should be array([10, 18, 24, 28, 30, 30, 28, 24, 18, 10]))
#Extract the diagonal offset by 1 upwards (this should be array([ 2, 6, 12, 20, 30, 42, 56, 72, 90]))

 
#6. Broadcasting

#Use broadcasting to create a grid of distances.