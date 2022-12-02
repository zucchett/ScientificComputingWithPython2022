#!/usr/bin/env python
# coding: utf-8

# Ceren Yılmaz Gülten Exercise 4 

# In[10]:


# 1. Reductions
import numpy as np
m = np.arange(12).reshape((3,4))
print("Matrix:",m)
print("Total mean of matrix:", m.mean())
print("Each Column mean:",m.mean(axis=0)) # axis=0 gives column 
print("Each Row mean",m.mean(axis=1)) # axis=1 gives row 


# In[81]:


# 2. Outer product
import numpy as np 

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

# a. numpy.outer

m = np.outer(u,v)
print("With Outer Product Function:\n", m)

# b. for loop or list compherension 

arr = [[u[j]*v[i] for i in range(len(u))] for j in range(len(v))]
print("With list compherension:\n",arr)

# c. broadcasting operation 

z = u*v
print("With vroadcasting operation:\n",z)


# In[157]:


# 3. Matrix masking
import numpy.random as npr 
import numpy as np 
# using random.uniform since in the question flat distribution and there is a limit 
# in rand function the function generate uniform distribution directly between 0-1
matrix = np.random.uniform(0,4,(10,6))
print("10x6 Random Float Matrix between 0-3:\n",matrix)
print("\n")
mask = (matrix<0.3)
print("Mask of Matrix for Values smaller than 0.3:\n",mask)
matrix[mask] = 0
print("\n")
print("Modified Matrix accroding to mask:\n",matrix)



# In[10]:


# 4. Trigonometric functions
import numpy as np 
import math
import matplotlib.pyplot as plt
a = np.linspace(0,2*(math.pi),100, endpoint=True)
print("Original array:\n",a)
print("\n")
b=a[9:100:10]
print("Every 10th element with slicing:\n",b)
print("\n")
c = a[::-1]
print("Reverse the original array:\n",c)
print("\n")

sin = np.sin(a)
cos = np.cos(a)
absolute = (abs(sin - cos))
filtered = a[absolute <0.1] 
print("Filtered version according to absolute value:\n",filtered)

plt.plot(a,sin)
plt.plot(a,cos)
plt.legend(['sin(x)', 'cos(x)']) 
idx = np.argwhere(np.diff(np.sign(sin - cos))).flatten() # to find intersection points
plt.plot(a[idx], sin[idx], 'ro' )
plt.plot(a[idx], cos[idx], 'bo')
plt.show()


# In[50]:


# 5. Matrices 
import numpy as np 


array = np.empty((10,10))

for i in range(0,10):
    for j in range(0,10):
        array[i][j] = (i+1)*(j+1)
print(array, '\n')


arr_trace = array.trace()
print("Trace of matrix:\n",arr_trace, '\n')

arr_anti = np.fliplr(array)
arr_anti = arr_anti.diagonal()
print("Anti-diagonal matrix:\n",arr_anti, "\n")

arr_upward = np.diag(array,1)
print("Diagonal offset by 1 upwards:\n",arr_upward,"\n")


# In[2]:


# 6. Broadcasting 
import numpy as np 
from matplotlib import pyplot

miles = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544,1913, 2448])
miles_t = miles[:, np.newaxis]
difference = abs(miles-miles_t)
print(difference)

pyplot.figure(figsize=(5,5))
pyplot.imshow(difference)
pyplot.colorbar()
pyplot.show()

a = [1.609344]
km = a*difference
print(km)


# In[35]:


#7. Prime numbers sieve
import numpy as np 
import time
t = 0 
start = time.time()
prime_arr = [True for i in range(100)] # boolean array for mask 
for i in range(100):
    if i<2:
        prime_arr[i] = False # first two index is False since 0 and 1 is not a prime number 
for i in range(2,100):  
    for j in range(2, i): 
        if (i % j) == 0: # if the numbers between 2 to 100 can divide any number between 2 to i its not a prime number so false
            prime_arr[i] = False
            break 
print(prime_arr)
prime_num = [i for i in range(100) if prime_arr[i]] # to remove the mask and show the values True values written as a number
print(prime_num)
end = time.time()
t = end - start 
print('Prime Number Nomral Method time:')
print(t, ' seconds')

# Sieve of Eratosthenes
t_1 = 0
start_1 = time.time()
prime_arr = [True for i in range(100)] # create boolean array 
k = 2 # define 2 because the prime numbers start from 2 
while (k * k <= 99): # it will continue until k=9 since until 9 we will look at all the power's of the numbers 
    if (prime_arr[k] == True): # checking if it is true or nut
        for i in range(k * 2, 100, k): # if its true check the all power of the value until 100 and write False for them
            prime_arr[i] = False # because they can divide to k so its not a prime number 
    k += 1 # increased the k value to check every value until 100 
prime_arr[0] = False
prime_arr[1] = False
prime_num = [i for i in range(100) if prime_arr[i]]# to remove the mask and show the values True values written as a number
print(prime_num)
end_1 = time.time()
t_1 = end_1 - start_1
print('Sieve of Erostosthenes Time:')
print(t_1, ' seconds')


# In[30]:


# 8. Diffusion using random walk
import random 
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import math 
walk_array = np.random.randint(-1,1, size=(1000,200))
walk_array = walk_array*2 + 1 # to get 1 and -1 

walk_distance = np.cumsum(walk_array, axis=1)

sqr = pow(walk_distance,2)

mean_walk = np.mean(sqr , axis =0)

print(mean_walk)

