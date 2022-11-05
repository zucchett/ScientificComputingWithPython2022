# Reductions

import numpy as np

m = np.arange(12).reshape((3,4))
print("The matrix is:\n" + str(m))

meantot = np.mean(m)
meanrow = np.array([np.mean(m[i,:]) for i in range(3)])
meancol = np.array([np.mean(m[:,i]) for i in range(4)])

print("The total mean of the matrix elements is " + str(meantot))
print("The mean for each row is " + str(meanrow))
print("The mean for each column is " + str(meancol))
