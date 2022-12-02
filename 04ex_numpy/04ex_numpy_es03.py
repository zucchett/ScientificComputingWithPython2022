
# 3. Matrix masking

# Create a 10 by 6 matrix of float random numbers, distributed between 0 and 3 
# according to a flat distribution.

# After creating the matrix, set all entries  to zero using a mask.

# -------------------------------------- Code Begin-------------------------------------
import numpy as np

u = np.random.uniform(low=0, high=3, size=(10,6))
mask = u > 0.3
print('A flat distributed Matrix before Matrix Masking : \n', u)
print('\n ------------------------------------------- \n')
print('A flat distributed Matrix after Matrix Masking : \n', u*mask)

# -------------------------------------- Code End---------------------------------------
