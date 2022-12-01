# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 12:56:09 2022

@author: UmutBerkCakmakci
"""

import numpy as np
import math
import numpy.random as npr
import timeit
import matplotlib.pyplot as pyp
from tabulate import tabulate
from timeit import timeit as tit

np.set_printoptions(threshold=np.inf)

# 04ex_numpy_es01
"""
print("\n04ex_es01 answer:\n--------------------------------------------------")

m = np.arange(12).reshape((3,4))
print(m)
print("total mean:", m.mean())
print("means of each column, respectively:", m.mean(axis=0))
print("means of each row, respectively:", m.mean(axis=1))
"""

# 04ex_numpy_es02
"""
print("\n04ex_es02 answer:\n--------------------------------------------------")

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

print("\nEx04_es02_partA_solution:\n")
res1 = np.outer(u, v)
print(res1)

print("\nEx04_es02_partB_solution:\n")
res2=[]

for i in range(0,len(u),1):
    for j in range(0,len(v),1):
        res2 = np.append(res2, v[j]*u[i])

res3=res2.reshape(4,4)
print(res3)

print("\nEx04_es02_partC_solution:\n")
m = np.tile(v, (4,1))
n = u.reshape(4,1)
print(m*n)
"""

# 04ex_numpy_es03
"""
print("\n34ex_es04 answer:\n--------------------------------------------------")

a=npr.uniform(0, 3, size=(10, 6))
print("The original array:\n",a)

mask = (a<0.3)
print("\nThe mask:\n", mask, '\n')

filtered_a = a[mask]
print("The filtered array:\n", filtered_a, '\n')

a[a<0.3] = 0
print("The modified array:\n", a, '\n')
"""

# 04ex_numpy_es04
"""
print("\n04ex_es04 answer:\n--------------------------------------------------")

a=np.linspace(0, 2*math.pi, 1000)
#print(a)
b=a[::10]
#print(b)
c=b[::-1]
#print(c)
g=[]
d_list = []
e_list = []
for i in range(len(c)):
    d=math.sin(c[i])
    d_list=np.append(d_list, d)
    e=math.cos(c[i])
    e_list=np.append(e_list, e)
    f=abs(d-e)
    #print(f)
    if(f<0.1):
        g=np.append(g,f)
print("The sinus values: ", d_list, 
      "\nThe cosinus values: ", e_list, 
      "\nThe absolue difference of them: ", g)
pyp.plot(d_list, label = "sin")
pyp.plot(e_list, label = "cos")
pyp.xlabel("The numbers, respectively")
pyp.ylabel("Values")
pyp.legend()
pyp.show()
"""

# 04ex_numpy_es05
"""
print("\n04ex_es05 answer:\n--------------------------------------------------")

a = np.arange(1, 11, 1)
res1=np.outer(a,a.T)
print("The original matrix is:\n", res1)
res2=np.trace(res1)
print("\nThe trace of the matrix is:\n", res2)
res3=np.diag(np.fliplr(res1))
print("\nThe anti-diagonal of the matrix is:\n", res3)
res4=np.diag(res1, 1)
print("\nThe diagonal offset by +1 upwards is:\n", res4)
"""

# 04ex_numpy_es06
"""
print("\n04ex_es06 answer:\n--------------------------------------------------")

city1 = np.array(['Chicago', 'Springfield', 'Saint-Louis', 'Tulsa', 'Oklahoma_City', 
                  'Amarillo', 'Santa_Fe', 'Albuquerque', 'Flagstaff', 'Los_Angeles'])
dist = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
dist2=np.round(dist*1.609344, 1)
city2=city1.T
table = ['']
table = np.append(table, city1)
ab=len(table)

for i in range(1, ab, 1):
    asd = np.round(abs(dist2[i-1]-dist2),1)
    table=np.append(table, table[i])
    table=np.append(table, asd)

table=table.reshape((11,11))
print(table)
print(tabulate(table))
"""

# 04ex_numpy_es07
"""
print("\n04ex_es07 answer:\n--------------------------------------------------")

def prime_sieve(n):
    prime = []
    era = [0 for i in range(n+1)]
    for i in range(2, n+1):
        if(era[i] == 0):
            prime.append(i)
            k = i + i
            while(k < n+1):
                era[k] = 1
                k += i

def Eratosthenes_optimization(N):
    nums = np.arange(2, N+1, 1)
    mask2 = np.arange(2, N+1, dtype = int)
    for n in nums:
        for i in np.arange(2*n-2, N-1, n):
            mask2[i] = 0
    return nums, mask2  

n=int(input("Please enter a valid N value: "))

numbers, mask2 = Eratosthenes_optimization(n)
mask2 = mask2[mask2 != 0] # Prime number list

#print(mask2, len(mask2))
print("\nThe time for normal solution is: ", tit('prime_sieve', globals=globals(), number=1))
print("--> Comment: The time increases slightly when we increase the upper limit (N) of the function.",
      "But if we choose N very large numbers (i.e. 10M) we can see the real difference.\n")
print(f"The time for optimized method is: {timeit.timeit('mask2', globals=globals(), number=1)}")
print("--> Comment: The time is less than normal solution with the optimized method.",
      "But if we wanna see the real difference, we need to choose n very large numbers (i.e. 10M).")
"""

# 04ex_numpy_es08
""
print("\n04ex_es08 answer:\n--------------------------------------------------")

a=npr.randint(0, 2, size=(1000, 200))
mask = (a==0)
a[mask]=-1
#print(a)
x = npr.choice([-1, 1], size=(1000,200))
#print(x)

# I create dataset with 2 different ways; 
# one is using numpy.random.randint and mask method, 
# the other is using numpy.random.choice method (this method is easier in this case). 

y=x.sum(1)
print("\nsum along the rows:\n", y)
y2=y**2
print("\nsquraed sums:\n", y2)
y22=abs(y)
y3=x.mean(axis=0)
print("\nmeans along the columns of original array:\n", y3)
pyp.plot(y22)
pyp.show()
#for i in range(len(y2)):
    #print("Walker number ",i+1 , " is walked ", y2[i], " steps!")
""

