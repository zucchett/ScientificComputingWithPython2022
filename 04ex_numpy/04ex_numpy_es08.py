#8. Diffusion using random walk

import numpy as np

#1000 walkers walk for 200 steps
walkers=1000
steps=200
a=np.random.randint(0,2,(walkers,steps))
a[a==0]=-1

#The walking distances for each walker
walking_distances = a.sum(axis=1)
print('the walking distances for each walker are:\n',walking_distances)

#The square of the walking distances
walking_distances_squared=np.square(walking_distances)

#The mean of the squared distances at each step
mean_squared_distances=np.mean( np.cumsum(a, axis=1)**2 , axis=0)
print('the walking distances for each walker are:\n',mean_squared_distances)
