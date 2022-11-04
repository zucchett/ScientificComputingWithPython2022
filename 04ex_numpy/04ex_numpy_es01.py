
# 1. Reductions

# Find the total mean, and the mean for each row and column of the following matrix:

# m = np.arange(12).reshape((3,4))
# -------------------------------------- Code Begin-------------------------------------
import numpy as np

m = np.arange(12).reshape((3,4))

print('The Total mean is : ',m.mean())
print('The mean of each row : ',m.mean(axis=1) )
print('The mean of each column : ',m.mean(axis=0))
# -------------------------------------- Code End---------------------------------------
