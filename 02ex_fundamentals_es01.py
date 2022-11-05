
def f(alist):
    x = 5
    blist = []
    for i in range(x):
        blist.append(i)
    return blist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed
