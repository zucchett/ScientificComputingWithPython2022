"""
2\. **Outer product**
Find the outer product of the following vectors:
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
Use different methods to do this:
   1. Using the function `outer` in numpy
   2. Using a nested `for` loop or a list comprehension
   3. Using numpy broadcasting operations
"""

import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

# 1. Using the function `outer` in numpy
outer_np = np.outer(u, v)
print(outer_np)

# 2. Using a nested `for` loop or a list comprehension
demo = []
for x in range(len(u)):
    temp = []
    for y in range(len(v)):
        temp.append(u[x]*v[y])
    demo.append(temp)

list_outer = np.array(demo)
print(list_outer)

#qs: how to use list comprehension to write the list
# outer_list = np.array([u[x]*v[y]]for x in range(len(u)) for y in range(len(v)) if y == 4)
# print(outer_list)

# 3. Using numpy broadcasting operations
u2 = u.reshape(-1, 1) # 在Numpy中将行向量转换为列向量
uu = np.repeat(u2, 4, axis=1)  # numpy.repeat(a, repeats, axis=None(转为1维向量)) a:object.repeats:The number of repetitions for each element
uuv_ba = uu*v
print(uuv_ba)


