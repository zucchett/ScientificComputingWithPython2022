#!/usr/bin/env python
# coding: utf-8

# In[12]:


# task 1
import numpy as np
m = np.arange(12).reshape((3,4))
print("Total mean" , m.mean())
Column_mean = np.mean(m,axis=0)
Row_mean = np.mean(m,axis=1)
print(Column_mean)
print(Row_mean)


# In[15]:


# task 2 
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

#outer function 
result = np.outer(u,v)
print(result,"\n")

#nested for loop
V = []
for i in u:
    row = []
    for j in v:
        row.append(i * j)
    V.append(row)
print(V,"\n")

#numpy broadcasting
u_v =u * v.reshape(4,1)
print(u_v.transpose())


# In[17]:


#task 3
start = np.linspace(0, 0.9,10)
end = np.linspace(5, 5.9,10)

M = np.linspace(start,end,6)
print(M)

print("\n entries with a decimal part  <0.4")
for i in range(0,4):
    M[:,i] = [0]

print(M)


# In[19]:


#task 4

arr1 = np.linspace(start = 0, stop = np.pi*2, num=100, endpoint=True, retstep=False, dtype=None, axis=0)
arr_reversed = arr1[::-1]
print("Reverse using the slice notation \n" +str(arr_reversed))
arr_10th = arr1[::10]
print("\n Extract every 10th element using the slice notation \n"+str(arr_10th))

arr_sin_cos = np.where(np.absolute(np.sin(arr1)-np.cos(arr1))<0.1,arr1,None)

arr_sin_cos = set(arr_sin_cos)
arr_sin_cos.remove(None)
print("Extracted elements absolute difference between the sin and cos functions for  <0.1: \n"+ str(arr_sin_cos))


# In[20]:


#task 5

x = [[i*j for j in range(1,11)] for i in range(1,11)]    
y = np.array(x).reshape(10,10)
print("10 * 10 Matrix: \n", y)
print("Trace of the matrix: ",np.sum(np.diag(x)))

rev_y = np.fliplr(y)
print("Anti-diagonal matrix: ",np.diag(rev_y))
print("Diagonal offset by 1 upwards: ",np.diag(y,1))


# In[22]:


#task 6

import matplotlib.pyplot as plt
import numpy as np
mile=np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
print("distance in miles:",mile)
distance= np.abs(mile-mile[:, np.newaxis])
print("distance ","\n",distance)
dis_km = d*1.609344
print("distance in km:","\n" ,dis_km.round(2))


# In[23]:


#task 7

def sieve(N):                    
    mask = np.ones(N, dtype=bool)     
    mask[:2] = False
    for i in range(2, N):
        mask[2*i::i] = False
    return np.arange(N)[mask]
N=100
print(sieve(N))

def sieve_er(N):
    mask = np.ones(N, dtype=bool)
    mask[:2] = False
    p = 2
    while (p * p <= N):
        if (mask[p] == True):
            for i in range(p * p, N, p):
                mask[i] = False
        p += 1
    return np.arange(N)[mask]
print(sieve_er(N))


# In[26]:


#task 8

walkers = 1000
steps = 200
walk = np.random.randint(low=0, high=2, size=(1000,200))
walk[walk==0]=-1
print("Walk: \n",walk)

distances = walk.cumsum(axis=1)
print("Steps sum: \n",distances)

sqr = np.square(distances)
print("Square of steps sum: \n", sqr)

arrmean=np.mean(sqr,axis=0)
print("Mean of squared distances at each step: \n", arrmean)


sqrrt = np.sqrt(arrmean)
plt.plot(np.arange(1,201),sqrrt)
plt.title('average distances vs time')
plt.xlabel('Time(steps)')
plt.ylabel('Average Distance')

