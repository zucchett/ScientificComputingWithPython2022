"""
1. Global Variables
Convert the function  into a function thatdoesn't use global variables and that does not modify the original list

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
