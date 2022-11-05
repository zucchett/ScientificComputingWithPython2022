# 8. Diffusion using random walk

# Consider a simple random walk process: at each step in time, a walker jumps right or left (+1 or -1) with equal probability. The goal is to find the typical distance from the origin of many random walkers after a given amount of time.

# Hint: create a 2D array where each row represents a walker, and each column represents a time step.

# Take 1000 walkers and let them walk for 200 steps
# Use randint to create a 2D array of size  with values -1 or 1
# Calculate the walking distances for each walker (e.g. by summing the elements in each row)
# Take the square of the previously-obtained array (element-wise)
# Compute the mean of the squared distances at each step (i.e. the mean along the columns)
# Optional: plot the average distances () as a function of time (step)

# -------------------------------------- Code Begin-------------------------------------
import numpy as np
import matplotlib.pyplot as plt

walkers = 1000
steps = 200

# Multipling by two and substracting 1 so the random integers {0,1} become {-1,1}
randomwalks = 2* np.random.random_integers(0,1,(walkers, steps)) - 1 
distance = np.cumsum(randomwalks, axis=1)
msd = np.mean(distance**2, axis=0)

plt.figure(figsize=(10, 10))
plt.plot(np.arange(steps), msd)
plt.xlabel('time')
plt.ylabel('average distance')


# -------------------------------------- Code End---------------------------------------
