#1.Global variables
def f(alist):
    x=5
    blist=[]
    for i in range(len(alist)):
       blist.append(alist[i])

    for i in range(x):
        blist.append(i)
    return blist

alist = [1, 2, 3]
ans = f(alist)
print(ans, "list id:" ,id(ans))
print(alist, "list id:", id(alist)) # alist has been changed
print("alist has been changed")


