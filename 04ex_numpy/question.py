"""
es02-2:#qs: how to use list comprehension to write the list 用列表理解怎么写那个for循环

es03:what is flat distribution :正态分布randn和均匀分布是不是不一样，用哪个函数才是正确的

es04:how to Extract every 10th element using the slice notation  怎么每隔10分割，
    & the absolute difference between the `sin` and `cos` 以及sin和cos那个部分要怎么理解

es06&es07 理解

es08:walkers = np.random.randint(-1, 1, size=(10, 2)) 只取得1和-1
"""

# x = np.empty([10,6], dtype = float)

# # generic diagonal matrix
# diagonal = np.diag(np.array([1, 20, 3, 4]))
# print(diagonal, '\n')
#
# # from list comprehensions
# array = np.array([(i, j) for i in range(2) for j in range(3)])
# print(array, '\n')
#
# # from a function
# fromfunct = np.fromfunction(lambda i, j: (i - 2) ** 2 + (j - i) ** 2, (5, 5))
# print(fromfunct, '\n')