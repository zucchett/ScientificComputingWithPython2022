# Matrix masking

import numpy as np

m = np.random.uniform(0., 3., (10,6))
print(m, "\n")

m[m < 0.3] = 0.
print(m)
