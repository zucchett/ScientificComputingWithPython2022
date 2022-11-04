

def f(alist):
    x = 5
    k = alist[:]
    for i in range(x):
        k.append(i)
    return k

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) 
