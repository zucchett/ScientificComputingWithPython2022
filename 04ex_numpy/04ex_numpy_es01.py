import numpy as np

m = np.arange(12).reshape((3,4))
print(m)

print(np.mean(m))
c = np.mean(m, axis = 0)
d = np.mean(m, axis = 1)
print(c)
print(d)