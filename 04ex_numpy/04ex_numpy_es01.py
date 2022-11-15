"""
1.Reductions
Find the total mean, and the mean for each row and column of the following matrix:
m = np.arange(12).reshape((3,4))
求总的平均数，以及以下矩阵的每一行和每一列的平均数。
"""
import numpy as np

m = np.arange(12).reshape((3, 4))
print(m)
total_mean = np.mean(m)
row_mean = np.mean(m, axis=1)
column_mean = np.mean(m, axis=0)

print(f"total mean is {total_mean},the mean for each row is {row_mean},the mean for each column is{column_mean}")

