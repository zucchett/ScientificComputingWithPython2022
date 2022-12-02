"""
8.Diffusion using random walk
Consider a simple random walk process: at each step in time, a walker jumps right or left (+1 or -1) with equal
probability. The goal is to find the typical distance from the origin of many random walkers after a given
amount of time.
*Hint*: create a 2D array where each row represents a walker, and each column represents a time step.
  * Take 1000 walkers and let them walk for 200 steps
  * Use `randint` to create a 2D array of size walkers * steps with values -1 or 1
  * Calculate the walking distances for each walker (e.g. by summing the elements in each row)
  * Take the square of the previously-obtained array (element-wise)
  * Compute the mean of the squared distances at each step (i.e. the mean along the columns)
  * **Optional**: plot the average distances ($\sqrt(distance^2)$) as a function of time (step)
考虑一个简单的随机行走过程：在时间的每一步，一个行走者以相等的概率向右或向左（+1或-1）跳跃。
概率。我们的目标是找到许多随机行走者在给定时间后与原点的典型距离。
的典型距离。
*提示*：创建一个二维数组，每一行代表一个步行者，每一列代表一个时间步骤。
  * 取1000个步行者，让它们步行200步
  * 使用`randint`创建一个大小为$walkers /times steps$的二维数组，值为-1或1
  * 计算每个步行者的步行距离（例如，通过对每一行的元素求和）。
  * 取先前获得的数组的平方（从元素上看）。
  * 计算每一步的距离平方的平均值（即沿列的平均值）
  **可选**：绘制平均距离（$sqrt(distance^2)$）与时间（步长）的关系图
"""
import numpy as np

walkers = np.random.randint(0, 2, size=(10, 2))
walkers = walkers * 2 - 1
# dataset = np.asarray(walkers)
# dataset = dataset * 2 -1
print(walkers)
# row_sum = np.sum(walkers, axis=0)
# squ_ary = np.square(row_sum)
# column_mean = np.mean(walkers, axis=0)
# print(f"2D array of size walkers * steps\n{walkers}\n"
#       f"the walking distances for each walker by summing the elements in each row\n{row_sum}\n"
#       f"the square of the previously-obtained array\n{squ_ary}\n"
#       f"the mean of the squared distances at each step\n{column_mean}\n"
#       )
