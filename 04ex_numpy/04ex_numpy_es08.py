import numpy as np
x = np.random.choice([-1,1],(1000,200))
print("This is the random numbers:", x)
dists = np.sum(x,axis = 0)
print("\nThese are the distances:\n", dists.T)
squared_dist = dists ** 2
mean =  (squared_dist).mean()
print("\nThis is the mean:\n", mean)
