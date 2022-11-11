"""
5. Matrices
Create a matrix that shows the 10 by 10 multiplication table.
Find the trace of the matrix
Extract the anti-diagonal matrix (this should be array([10, 18, 24, 28, 30, 30, 28, 24, 18, 10]))
Extract the diagonal offset by 1 upwards (this should be array([ 2, 6, 12, 20, 30, 42, 56, 72, 90]))
"""

import numpy as np

a = np.ones((10, 10))
b = np.linspace(1, 10, 10)
matrix = np.outer(b, b.T)
print(matrix)  # built the matrix

trace = 1
antidiag = np.array([])
offdiag = np.array([])
for i in range(10):
    trace = trace * matrix[i][i]  # find the trace
    antidiag = np.append(antidiag, matrix[i][9 - i])  # find anti-diagonal matrix
    try:
        offdiag = np.append(offdiag, matrix[i + 1][i])  # find offset 1 diagonal
    except:
        print("\n  ################################################### \n")
print("\nTrace:  ", trace)
print("\nAnti-diagonal matrix:  ", antidiag)
print("\nDiagonal offset 1:  ", offdiag)
