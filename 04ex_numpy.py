# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:27:02 2022

@author: 10
"""
import numpy as np

#%%QUESTION 1

m = np.arange(12).reshape((3,4))

#mean for each row
for i in range(len(m)):
    print( i+1 ,  "th row's mean is " , np.mean(m[i]))

#mean for each column
for i in range(len(m[0])):
    print(i+1 , "th column's mean is " , np.mean(m[:,i]))

#arrays mean
print( " Array's mean is ",np.mean(m))

#%%QUESTION 2
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

#1st method
print( "with outer numpy \n",np.outer(u,v))

#2nd method nested for loop
product_2 = []
for i in u:   
    row = []
    for j in v: 
        row.append(i * j)
    product_2.append(row)
print( "with nested loop ",product_2)
#2nd method list comp
product_2_comp = [i*j for i in u for j in v]
print( "with list compherension",product_2_comp)

#3rd
product_3 = u*v
print( "with broadcasting ", product_3 )

#%%QUESTION 3
a=np.random.uniform(0,3,(10, 6))
mask = a > 0.3 
print(mask) #the mask array
new= a[mask]
print(a[mask]) #the filtered array
a[a < 0.3] =0  #filling with 0s
print(a)       
#%%QUESTION 4
import math
import matplotlib.pyplot as plt

x= np.linspace(0,2*math.pi,100)
x_sliced = x[9:100:10]
x_reversed = x[::-1]

cosine = np.cos(x)
sine = np.sin(x)

T= []
diff = abs(cosine-sine)
print( "index|the value")
for i in range(len(diff)):
    if diff[i] <0.1:
        T.append(x[i])
        print(i,x[i])
        

plt.plot(x,sine,x,cosine)
plt.plot(T,np.cos(T), marker= 'o') # The intersection points where the diff is <0.1, there are 4 points
plt.show()
#%%QUESTION 5
import numpy as np

fromfunct = np.fromfunction(lambda i,j: i*j, (11, 11))
x = np.delete(fromfunct, (0), axis=0)
x = np.delete(x,(0), axis=1)
print(x)

trace = np.trace(x)
print(trace)

diagonal_reverse = np.fliplr(x).diagonal()
print(diagonal_reverse)

diagonal_upper = np.diag(x,1)
print(diagonal_upper)

#%%QUESTION 6
import numpy as np
import matplotlib.pyplot as plt

y = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
t = y.reshape(len(y),1)
distances = abs(y-t)
print(distances)

km =[1.609344] #1 mile equals 1.609344 km
kilometer_conversion= distances*km

#%%QUESTION 7
import numpy as np 
import time
t_1 = 0 
start = time.time()
prime = [True for i in range(100)]
for i in range(100):
    if i<2:
        prime_arr[i] = False 
for i in range(2,100):  
    for j in range(2, i): 
        if (i % j) == 0: 
            prime[i] = False
            break 
print(prime)
numbers_prime = [i for i in range(100) if prime[i]] 
print(numbers_prime)
end = time.time()
t_1 = end - start 
print('Prime Number Nomral Method time:')
print(t_1, ' seconds')

# Sieve of Eratosthenes
t_2 = 0
start_2 = time.time()
prime_2 = [True for i in range(100)] 
k = 2 
while (k * k <= 99): 
    if (prime_arr[k] == True): 
        for i in range(k * 2, 100, k): 
            prime_2[i] = False 
    k += 1 
prime_2[0] = False
prime_2[1] = False
numbers_prime_2 = [i for i in range(100) if prime_2[i]]
print(numbers_prime_2)
end_2 = time.time()
t_2 = end_2 - start_2
print('Sieve of Erostosthenes Time:')
print(t_2, ' seconds')

#%% QUESTION 8
import numpy as np
import random
from random import randint
import matplotlib.pyplot as plt

# newArray = np.random.randint(-1,1, size=(1000,200))
# newArray= newArray*2 +1

array_2D =2*(np.random.randint(0,2,size=(1000,200)))
array_2D = array_2D -1

array_walk_dist = np.cumsum(array_2D, axis=1)

squared_array = array_walk_dist**2

mean = np.mean(squared_array , axis =0)

plt.plot(np.arange(200), np.sqrt(mean))
