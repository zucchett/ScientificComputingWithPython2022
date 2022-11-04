ef f(alist):
    x = 5
    alist=[1,2,3]#re assigned to new object, so the original list will not change
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
alist2=alist
ans = f(alist2)
print(ans)
print(alist) # alist has NOT been changed