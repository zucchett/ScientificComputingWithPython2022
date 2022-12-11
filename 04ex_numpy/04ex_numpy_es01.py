#1. Reductions

import numpy as np

m = np.arange(12).reshape((3,4))

print('Matrix m : \n',m)

print("The total mean of the matrix m:",m.mean())

print("The mean for each row goes as follow:",np.mean(m, axis=1))

print("The mean for each column goes as follow:",np.mean(m, axis=0))
