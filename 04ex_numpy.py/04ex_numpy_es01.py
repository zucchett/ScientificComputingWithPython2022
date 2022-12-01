import numpy as np
m = np.arange(12).reshape((3,4))
print(m)
print(m.mean())
print(m.mean(0))
print(m.mean(1))