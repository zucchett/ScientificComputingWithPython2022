x = 5

def f(alist):
    for i in range(x):
        alist = alist + [i]
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed