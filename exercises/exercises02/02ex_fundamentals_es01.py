

def f(alist):
    x = 5
    alist = [1, 2, 3]
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has not been changed