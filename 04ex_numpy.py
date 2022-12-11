# 04ex_numpy by Alberto Merotto 208117
#*************************************************************
#Exercise 01:

import numpy as np
m = np.arange(12).reshape((3,4))
print('m: ', '\n', m, '\n')
print('total mean: ', np.mean(m)) #total mean

for i in range(m.shape[0]):			#mean of each row
	print('mean of row ',i, ': ', np.mean(m[i]))
	
for i in range(m.shape[1]):			#mean of each column
	print('mean of column ',i, ': ', np.mean(m[:,i]))
	
#*************************************************************
#Exercise 02:
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
print('vector u: ', u)
print('vector v: ', v)

r = np.outer(u, v)  #using numpy.outer()
rl = np.array([u[a]*v[j] for a in range(len(u)) for j in range(len(v))]).reshape(len(u), len(v)) #using list comprhension
print(r)
print(rl)

print(u.reshape(u.shape[0], 1)*v) #using broadcasting

#*************************************************************
#Exercise 03:
import numpy.random as npr
npr.seed(2081117)

#generating random matrix:
rm = npr.uniform(0, 3, size=(10, 6))
print('random matrix: \n', rm)

#creating the mask:
mask = rm<0.3
#using the mask to set all elements <0.3 to zero
rm[mask] = 0
print('random matrix after using the mask: \n', rm)
#alternatively, in just a single line:
rm[rm<0.3] = 0
print(rm)

#*************************************************************
#Exercise 04:
import matplotlib.pyplot as plt


s = np.linspace(0, (2*np.pi), 100)
print(s)
t = s[::10] #extracting every 10th element
print(t)
s = s[::-1] #reversing the array
print(s)
mask = abs((np.sin(s)-np.cos(s)))<0.1 #creating the mask to extract the desired elements
u = s[mask] #nparray with only the desired elements
print(u)

#plotting the functions and the lines where the two funcions are close
y=np.sin(s)
plt.plot(s,y)
y=np.cos(s)
plt.plot(s,y)
for element in u:
	plt.axvline(element, color = 'red', linestyle = '--')
plt.show()

#*************************************************************
#Exercise 05:
mat = np.fromfunction(lambda i, j: ((i+1)*(j+1)), (10,10))
print(mat)

#finding the trace:
trace = 0

for i in range(mat.shape[0]):
	for j in range(mat.shape[1]):
		if i==j:
			trace = trace + mat[i,j]
print(trace)
#alternatively, using built in method of numpy:
print(mat.trace())
#extracting the anti diagonal
ad = np.fliplr(mat).diagonal()
print(ad)
#extracting the diagonal with offset 1
od = mat.diagonal(offset=1)
print(od)


#*************************************************************
#Exercise 06:
distances = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
grid = abs(distances - distances.reshape(distances.shape[0], 1))  #transposing the vector to use broadcasting
print('Grid distances in miles: \n', grid)
grid_km = grid * 1.60934 #converting to km
print('Grid distances in km: \n', grid_km)

#*************************************************************
#Exercise 07:
import timeit
import math
N = 99
l = np.arange(N)

mask=[False for i in range(N)]

for i in range(2, N):
	prime = True
	for j in range(2, int(math.sqrt(i)+1)):
		if i%j==0:
			prime = False
	if prime:
		mask[i] = True


pn = l[mask]
print(pn)
#measuring the execution time
s="""
mask=[False for i in range(N)]

for i in range(2, N):
	prime = True
	for j in range(2, int((i)**(1/2)+1)):
		if i%j==0:
			prime = False
	if prime:
		mask[i] = True
"""
lns = np.linspace(100, 1000000, 30)
y = np.array([])
for j in lns:
	e3 = timeit.timeit(s, number=1, setup = 'N = '+str(int(j)))
	print('Time with N =', int(j), ':', e3)
	y = np.append(y, e3)

plt.plot(lns,y)
plt.show()
#the plot is the one of a quadratic function

#implementing Sieve of Eratosthenes algorithm
l_e = np.arange(N+1)
mask_e=[True for i in range(N+1)]

i=2
while(i**2<N):
	if mask_e[i]:
		for j in range(i**2, N+1, i):
			mask_e[j] = False
	i = i+1
mask_e[0]=False
mask_e[1]=False
pn_e = l_e[mask_e]
print(pn_e)

#measuring performance
t="""
N = 1000000
mask_e=[True for i in range(N+1)]

i=2
while(i**2<N):
	if mask_e[i]:
		for j in range(i**2, N+1, i):
			mask_e[j] = False
	i = i+1
"""
e2 = timeit.timeit(t, number=1)
print(e2)
#the Sieve of Eratosthenes is bay far the most efficient: with N = 1000000 the "standard" algorithm
#takes approximately 29 seconds, while the Sieve of Eratosthenes takes just 0.1 seconds
#so it is more efficient by two orders of magnitude

#*************************************************************
#Exercise 08:
N_walkers = 10
steps = 5
m = npr.randint(-1, 1, (N_walkers, steps))
m[m==0] = 1
print(m)
distances_w = np.array([])
for i in range(m.shape[0]):
	d = np.sum(m[i,:])
	distances_w = np.append(distances_w, d)
print(distances_w)

distances_w_sq=distances_w**2
print(distances_w_sq)

m_cs = np.cumsum(m, axis=1)
print(m_cs)
m_cs = m_cs**2
print(m_cs)
distances_s_sq = np.mean(m_cs, axis=0)
print(distances_s_sq)

plt.plot(np.arange(steps), distances_s_sq)
plt.show()

