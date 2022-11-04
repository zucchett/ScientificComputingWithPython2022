def f(alist):
    blist = []
    x = 5
    for i in range(len(alist)):
        blist.append(alist[i])
    for i in range(x):
        blist.append(i)
    return blist

alist = [1, 2, 3]
ans = f(alist)
print("The modified list is: ", ans)
print("The original list is: ", alist)
