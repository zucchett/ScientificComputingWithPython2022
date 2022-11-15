"""
1. Global variabl
Convert the function into a function that doesn’t use global variables and that does not modify the original list
将该函数转换为不使用全局变量的函数，并且不修改原始列表
x = 5
def f(alist):
    for i in range(x):
        alist.append(i)
    return alist
alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed
"""
x = 5


def f(alist):
    t_array = list(alist)
    for i in range(x):
        t_array.append(i)
    return t_array


alist = [1, 2, 3]
n_ans = f(alist)

print(alist)
print(n_ans)
