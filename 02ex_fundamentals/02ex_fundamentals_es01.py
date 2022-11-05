def f(alist, x):
    newlist = list(alist)
    for i in range(x):
        newlist.append(i)
    return newlist

alist = [1, 2, 3]
ans = f(alist, 5)
print(ans)
print(alist) # alist hasn't been changed
