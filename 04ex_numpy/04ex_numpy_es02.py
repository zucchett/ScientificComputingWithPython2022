#2. Outer product

import numpy as np
u = np.array([1, 3, 5, 7]) 
v = np.array([2, 4, 6, 8])

#The outer product using the function outer in numpy
w=np.outer(u,v)
print('The outer product of u and v using the function outer:\n' ,w)

#The outer product using a nested for loop 
w=np.zeros((len(u),len(v)))
for i in range(len(u)):
    for j in range(len(v)):
        w[i,j]=u[i]*v[j]
print('The outer product of u and v using a nested for loop:\n' ,w)

#The outer product using a list comprehension
w=np.array([ [u[i]*v[j] for j in range(len(v))] for i in range(len(u)) ] )
print('The outer product of u and v using a a list comprehension:\n' ,w)

#The outer product using numpy broadcasting operations
w=np.zeros((len(u),len(v)))
for i in range(len(u)):
    w[i,:]=u[i]*v 
print('The outer product of u and v using numpy broadcasting operations:\n' ,w)
