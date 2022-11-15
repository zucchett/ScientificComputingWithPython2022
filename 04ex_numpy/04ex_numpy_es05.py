"""
5.Matrices**
Create a matrix that shows the 10 by 10 multiplication table.
 * Find the trace of the matrix
 * Extract the anti-diagonal matrix (this should be array([10, 18, 24, 28, 30, 30, 28, 24, 18, 10])
 * Extract the diagonal offset by 1 upwards (this should be ```array([ 2,  6, 12, 20, 30, 42, 56, 72, 90])```)
 创建一个显示10乘10乘法表的矩阵。
 * 找到该矩阵的轨迹
 * 提取反对角线矩阵
 * 提取向上偏移1的对角线
"""

import numpy as np


def mult_table(n):
    temp = np.arange(1, n + 1)
    print(temp, temp[:, None])
    return temp * temp[:, None]


mult_ten = mult_table(10)

mat_trace = np.trace(mult_ten)

anti_diag = np.fliplr(mult_ten).diagonal()

up_diag = np.diagonal(mult_ten, offset=1)
print(f"the 10 by 10 multiplication table\n{mult_ten}\n"
      f"the trace of the matrix\n{mat_trace}\n"
      f"the anti-diagonal matrix\n{anti_diag}\n "
      f"the diagonal offset by 1 upwards \n{up_diag} ")
