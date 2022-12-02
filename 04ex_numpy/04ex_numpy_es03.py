import numpy as np

a = np.random.uniform(0, 3, (10, 6))
print(a)
mask = a < 0.3
a[mask] = 0
print(a)