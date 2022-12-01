"""
3\. **Matrix masking**

Create a 10 by 6 matrix of float random numbers, distributed between 0 and 3 according to a flat distribution.

After creating the matrix, set all entries $< 0.3$ to zero using a mask.
"""
import numpy.random as np

mat = np.uniform(0, 3, size=(10, 6))
print("Generated Matrix:\n", mat)
mask = (mat < 0.3)
masked_matrix = mat[mask]
print("After using a mask: \n", masked_matrix)
