
def f(alist):
    x = 5
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
alist_c = [1, 2, 3]
ans = f(alist_c)
print(ans)
print(alist)
print(alist_c)