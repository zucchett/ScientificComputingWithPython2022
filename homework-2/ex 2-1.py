# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 07:21:21 2022

@author: gozde
"""

x = 5
def f(alist, n):
    x = n
    print("x (local) = ", x)
    new_list = [item for item in alist]
    for i in range(x):
        new_list.append(i)
    return new_list


alist = [1, 2, 3]
ans = f(alist=alist, n=4)
print("x (global) = ", x)
print("ans = ", ans)
print("alist = ", alist)