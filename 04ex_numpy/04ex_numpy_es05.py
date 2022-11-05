# 5. Matrices

# Create a matrix that shows the 10 by 10 multiplication table.

# Find the trace of the matrix
# Extract the anti-diagonal matrix (this should be array([10, 18, 24, 28, 30, 30, 28, 24, 18, 10]))
# Extract the diagonal offset by 1 upwards (this should be array([ 2, 6, 12, 20, 30, 42, 56, 72, 90]))

# -------------------------------------- Code Begin-------------------------------------
import numpy as np

u = np.outer(np.arange(1,11),np.arange(1,11))

print('Matrix that shows the 10 by 10 multiplication table : \n ',u)
print('\n ------------------------------------------- \n')
print('Matrix trace : ', u.trace() )
print('\n ------------------------------------------- \n')
print('Extracting the anti-diagonal : ', np.fliplr(u).diagonal())
print('\n ------------------------------------------- \n')
print('Extracting the diagonal offset by 1 upwards : ', u[1:,:].diagonal())


# -------------------------------------- Code End---------------------------------------
