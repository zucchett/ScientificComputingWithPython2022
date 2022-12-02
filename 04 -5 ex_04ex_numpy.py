import numpy as np
S = range(1,11) 
H = range(1,11)

mat = [[i*j for j in S] for i in H]
mat = np.array(mat)
print(mat)

#Find the trace of the matrix
print("\nTrace of matrix:",np.trace(mat))

#Extract the anti-diagonal matrix
S= np.fliplr(mat).diagonal()
print("Anti-diagonal matrix:",S)

#Extract the diagonal offset by 1 upwards
print("Diagonal offset by 1 upwards:",np.diagonal(mat,1))