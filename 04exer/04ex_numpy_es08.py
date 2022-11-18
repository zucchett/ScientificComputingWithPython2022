#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import numpy as np
import numpy.random as npr
import random
import matplotlib.pyplot as plt
"""
#USA RANDRANGE
#walker = [[random.randrange(-1, 2, 2) for i in range(200)]for j in range(1000)]
walker = np.random.randint(0, 2, size=(1000, 200))
walker[walker == 0] = -1
print(walker)
print(len(walker))
print(len(walker[0]))
srow =  np.sum(walker, axis = 1)
squares = np.square(srow)
medie_squares = srow.mean(axis=0)
print(medie_squares)
#print(srow)
step = np.linspace(0, 200, 201)
print(step)
#scolumn = np.sum(walker, axis = 0)
#print(scolumn)
#print(len(scolumn))
"""


"""
walkers = 1000
steps = 200
walk_arr = np.random.randint(2, size=(walkers, steps))
walk_arr[walk_arr == 0] = -1
walking_distances = []
for i in walk_arr:
    walking_distances.append(np.sum(i))
print(walking_distances)
walking_distances_squarred = np.square(walking_distances)
mean_sum = 0
mean_distance_squarred = []
for i in walking_distances_squarred:
  mean_sum += i
mean_distance_squarred.append(np.mean(mean_sum))
distances = np.sqrt(walking_distances_squarred)
print(distances)
m = np.arange(0, len(distances))
x = np.linspace(0, 200, 201)

plt.plot(x, distances)
plt.show()
"""


import numpy as np
import matplotlib.pyplot as plt

# Generate uniform 1000x200 matrix of 0 and 1
m = np.random.randint(0, 2, size=(1000, 200))

# Change the 0s to -1
m[m == 0] = -1
#print(m)
# Initialising some arrays
p = np.zeros((1000,200), dtype=int) # Cumulative movement matrix
p2 = np.zeros((1000,200), dtype=int) # Cumulative movement squared matrix
progress = np.zeros(1000, dtype=int) # Auxiliary vector to fill p column by column

# Filling p using progress
for i in range(200):
	progress += m[:,i]
	p[:,i] = progress

print("Walking distances (signed distance from starting point) for each walker:")
#print(p[:,199])
#print(len(p))

p2 = p**2
distance2 = np.mean(p2, axis=0)

print("Metodo Leo:\n")
print(distance2)

distance = np.sqrt(distance2)
#print(len(distance))
#distance = np.concatenate([[0],distance])
x = np.linspace(0, 200, 200)

#print("\nPlot shows the average distance of the walker in function of the number of steps")
plt.plot(x, distance)
#plt.show()
#########################################################################
np.random.seed(10)
walkers_x = np.zeros((1000,200))
for i in range(walkers_x.shape[0]):
        mat = np.random.randint(-1,1,size=walkers_x.shape[1]) #produce -1,0\n",
        mat[mat==0]=1 #set the 0 to 1\n",
        walkers_x[i] = mat

#walkers_y = np.zeros((1000,200))
#for i in range(walkers_y.shape[0]):
#        mat = np.random.randint(-1,1,size=walkers_y.shape[1]) #produce -1,0\n",
#        mat[mat==0]=1 #set the 0 to 1\n",
#        walkers_y[i] = mat
#print(walkers_x)
#print(walkers_y)
sums_x = np.cumsum(walkers_x, axis=1)
sq_sums_x = sums_x**2
#print(sq_sums_x)
#print(sq_sums_x.shape)
means_x = np.mean(sq_sums_x**0.5, axis=1)
means_x = np.mean(sq_sums_x, axis=0)
#print(len(means_x))
x = np.linspace(0, 200, 200)
#plt_x = plt
#plt_x.plot(means_x)
print("Metodo tizio: \n",means_x)
plt.plot(x, np.sqrt(means_x))
plt.show()
#plt_x.plot(means_x**0.5)
#plt_x.show()
    
#sums_y = np.cumsum(walkers_y, axis=1)
#sq_sums_y = sums_y**2
#means_y = np.mean(sq_sums_y**0.5, axis=1)
#means_y = np.mean(sq_sums_y, axis=0)
#plt_y = plt
#plt_y.plot(means_y)
#plt_y.plot(means_y**0.5)
#plt_y.show()
    
#plt.plot(sums_x[0,:],sums_y[0,:])
   
  