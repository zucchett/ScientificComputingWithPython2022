def f(alist, x):
    b = list(alist)
    for i in range(x):
        b.append(i)
    return b

alist = [1, 2, 3]
x = 5
ans = f(alist, x)
print(ans)
print(alist) # alist has been changed