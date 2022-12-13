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
import numpy as np


#######################################

a = np.random.randint(2, size=(1000, 200))
a[np.where(a == 0)] = -1
print(a)
walking_dist = np.sum(a, axis=1)
print("walking distance of each walker:\n", walking_dist)
sq_a = np.power(walking_dist, 2)
print("element-wise square is:\n", sq_a)
# mean=sq_a.mean(axis=0)
# print("mean along columns :\n",mean)
mean = []
for i in range(1, 200):
    b = a[:, i].mean()  # mean will be calculated along each column here
    mean.append(b)
print("mean along the columns is:\n", mean)
average_distance = np.sqrt(sq_a)
print("average distances:\n", average_distance)
array = average_distance
time = np.sort(array)
plt.plot(time, array)
plt.xlabel('Time')
plt.ylabel('Average Distances')
