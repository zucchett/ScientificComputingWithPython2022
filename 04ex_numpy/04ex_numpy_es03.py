"""
3.Matrix masking**
Create a 10 by 6 matrix of float random numbers, distributed between 0 and 3 according to a flat distribution.
After creating the matrix, set all entries < 0.3 to zero using a mask.
创建一个10乘以6的浮动随机数矩阵，根据平坦分布在0和3之间分布。
在创建矩阵后，使用掩码将所有<0.3的条目设置为零。
"""
import numpy as np

a = np.random.uniform(0, 3, [6, 10]) #均匀分布
b = np.random.normal(0, 3, [6, 10])  #正态分布（高斯分布）
print(a, '\n')

a[a < 0.3] = 0

print(f"the result of using mask is {a}")


