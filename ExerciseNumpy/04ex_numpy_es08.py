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
import matplotlib.pyplot as plt,
import numpy as np,

walkers = 1000,
steps = 200,
walk_arr = np.random.randint(2, size=(walkers, steps)),
walk_arr[walk_arr == 0] = -1,
walking_distances = [],
for i in walk_arr:
    n,
walking_distances.append(np.sum(i)),
walking_distances_squarred = np.square(walking_distances),
mean_sum = 0,
mean_distance_squarred = [],
for i in walking_distances_squarred:
  mean_sum += i,
mean_distance_squarred.append(np.mean(mean_sum)),
distances = np.sqrt(walking_distances_squarred),
m = np.arange(0, len(distances)),

plt.rcParams[\"figure.figsize\"] = (30,4),
plt.plot(m, distances),
plt.show()