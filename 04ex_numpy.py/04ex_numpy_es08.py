# We start at origin (x=0,y=0) and take random steps in each direction giving us 9 possible directions for movement at each step (∆x, ∆y ) ⋲ {-1, 0, 1} :

# (-1,-1), (-1,0), (-1,1),
# (0,-1), (0,0), (0,1),
# (1,-1), (1,0), (1,1)
import numpy as np
import matplotlib.pyplot as plt
# Define parameters for the walk
dims = 2
step_n = 10000
step_set = [-1, 0, 1]
origin = np.zeros((1,dims))
print(origin)
# Simulate steps in 2D
step_shape = (step_n,dims)
steps = np.random.choice(a=step_set, size=step_shape)
print(steps)
path = np.concatenate([origin, steps]).cumsum(0)
print(path)
start = path[:1]
stop = path[-1:]
# Plot the path
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.scatter(path[:,0], path[:,1],c='blue',alpha=0.25,s=0.05)
ax.plot(path[:,0], path[:,1],c='blue',alpha=0.5,lw=0.25,marker='+')
ax.plot(start[:,0], start[:,1],c='red', marker='*')
ax.plot(stop[:,0], stop[:,1],c='black', marker='o')
plt.title('2D Random Walk')
plt.show()