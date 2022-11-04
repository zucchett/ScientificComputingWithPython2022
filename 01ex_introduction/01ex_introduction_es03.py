# 3. Computing the distance
# Write a function that calculates and returns the euclidean distance between
# two points u and v in a 2D space, where u and v are both 2-tuples (x,y).
# Example: if u=(3,0) and v=(0,4), the function should return 5.
# Hint: in order to compute the square root, import the math library with import math and use math.sqrt().
# 3. 计算距离
# 编写一个函数，计算并返回以下两点之间的欧氏距离
# 二维空间中的两点u和v，其中u和v都是2元组(x,y)。
# 例子：如果u=(3,0)，v=(0,4)，这个函数应该返回5。

import math


def Distance(u, v):
    dis = math.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)
    return dis


u = (3, 0)
v = (0, 4)
print(Distance(u, v))
