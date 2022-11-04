x = 5

def f(alist):
    a=alist[:]
    for i in range(x):
        a.append(i)
    return a

alist = [1, 2, 3]
ans = f(alist)
print("Modified list: ",ans)
print("Original list: ",alist) # alist has been changed