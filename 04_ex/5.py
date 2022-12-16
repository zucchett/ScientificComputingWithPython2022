import numpy as np
M_1= range(1,11)
M_2= range(1,11)
A = [[i*j for j in M_1] for i in M_2]
A = np.array(A) # convert list to numpy array
print("\n :mult _table:\n",A)
print("\nTrace of matrix:",np.trace(A))
def anti_diagonal(arr):
    return np.fliplr(arr).diagonal()
print("\nAnti-diagonal matrix:\n",anti_diagonal(A))
print("\nDiagonal offset by 1 upwards:\n",np.diagonal(A,1))