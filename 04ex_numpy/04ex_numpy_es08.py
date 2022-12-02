import numpy as np

a = np.random.randint(2, size = (1000, 200))
a [a == 0] = -1
print(a)
distances = np.cumsum(a, axis = 1)
print(distances)
print(max(np.absolute(distances[:,-1])))
print(min(np.absolute(distances[:,-1])))
square_dis = distances * distances
print(square_dis)
mean_square_dis = np.mean(square_dis, axis = 0)
print(mean_square_dis)


import matplotlib.pyplot as plt
i = np.where(mask)     # Finding where sin and cos are close.
plt.plot(np.arange(200), np.sqrt(mean_square_dis), color = 'b', label = 'mean of average distances')
plt.legend()
plt.grid()
