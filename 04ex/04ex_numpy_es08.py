# Diffusion using random walk

import numpy as np
import matplotlib.pyplot as plt

# Generate uniform 1000x200 matrix of 0 and 1
m = np.random.randint(0, 2, size=(1000, 200))

# Change the 0s to -1
m[m == 0] = -1

# Initialising some arrays
p = np.zeros((1000,200), dtype=int) # Cumulative movement matrix
p2 = np.zeros((1000,200), dtype=int) # Cumulative movement squared matrix
progress = np.zeros(1000, dtype=int) # Auxiliary vector to fill p column by column

# Filling p using progress
for i in range(200):
	progress += m[:,i]
	p[:,i] = progress

print("Walking distances (signed distance from starting point) for each walker:")
print(p[:,199])

p2 = p**2
distance2 = np.mean(p2, axis=0)

print("\nMean of squared distances of the walkers at each step:")
print(distance2)

distance = np.sqrt(distance2)
distance = np.concatenate([[0],distance])
x = np.linspace(0, 200, 201)

print("\nPlot shows the average distance of the walker in function of the number of steps")
plt.plot(x, distance)
plt.show()
