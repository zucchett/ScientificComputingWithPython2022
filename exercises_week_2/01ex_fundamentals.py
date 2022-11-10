#1. Global variables

'''
x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed'''

x = 5

def f(alist,r):
    for i in range(r):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist,x)
print(ans)
print(alist) # alist has been changed