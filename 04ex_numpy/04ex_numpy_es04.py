"""
4.Trigonometric functions**
Use `np.linspace` to create an array of 100 numbers between 0and 2\pi (inclusive).
  * Extract every 10th element using the slice notation
  * Reverse the array using the slice notation
  * Extract elements where the absolute difference between the `sin` and `cos` functions evaluated for that
  element is < 0.1
  * **Optional**: make a plot showing the sin and cos functions and indicate where they are close
  4.三角函数
    使用`np.linspace`创建一个由100个数字组成的数组，这些数字介于0和2\pi(包括）之间。
  * 使用分片符号提取每10个元素
  * 使用分片符号对数组进行反转
  * 提取元素，其中对该元素评估的 "sin "和 "cos "函数之间的绝对差值为< 0.1。
  **可选**：制作一个显示sin和cos函数的图，并指出它们接近的地方。
"""
import numpy as np
# import matplot.pyplot as plt

# np.linspace(tart, stop, num=50, endpoint=True, retstep=False, dtype=None)
tri = np.linspace(0, 2 / np.pi, num=100, endpoint=True)

#Extract every 10th element using the slice notation
tri_ten =np.split(tri, 10)
tt = tri[::10]

print(tri_ten)


#Reverse the array using the slice notation
res = tri[::-1]
print(res)

#Extract elements where the absolute difference between the `sin` and `cos` functions evaluated for that element is < 0.1
ex_elements  = []
for x in np.nditer(tri):
    sin_result = np.sin(x)
    cos_result = np.cos(x)
    dif_abs= np.abs(sin_result - cos_result)
    if dif_abs < 0.1:
        ex_elements.append(x)
print(ex_elements, end=", ")
# plt.plot(x, dif_abs)
# plt.show()
#Optional**: make a plot showing the sin and cos functions and indicate where they are close
