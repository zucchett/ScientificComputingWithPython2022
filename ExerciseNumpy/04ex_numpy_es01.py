"""
1.Reductions
Find the total mean, and the mean for each row and column of the following matrix:
m = np.arange(12).reshape((3,4))
"""

import numpy as np

m = np.arange(12).reshape((3, 4))

print("\nTotal mean = ", np.mean(m))
for idx, row in enumerate(m):
    print("mean of row", idx, "=", np.mean(row))
for idx, col in enumerate(np.transpose(m)):
    print("Mean of column", idx, " = ", np.mean(col))
