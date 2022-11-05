x = 5

def f(alist,x):
    blist = [alist]
    for i in range(x):
        blist.append(i)
    return blist

alist = [1, 2, 3]
ans = f(alist,x)
print(ans)
print(alist)
