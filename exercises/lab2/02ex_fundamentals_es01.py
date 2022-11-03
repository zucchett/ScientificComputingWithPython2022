# Global variables

def f(alist):
    x = 5
    alist_new = [i for i in alist]
    for i in range(x):
        alist_new.append(i)
    return alist_new

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has not been changed