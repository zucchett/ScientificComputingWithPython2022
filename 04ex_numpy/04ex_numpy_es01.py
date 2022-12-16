import numpy as np
m = np.arange(12).reshape((3,4))
print("This is m:\n", m)
print("This is the total mean: ", np.mean(m))
print("This is the mean of each row:\n", np.mean(m, axis = 1))
