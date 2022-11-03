x = 5
def f(alist):
    blist = []
    for i in range(x):
         blist.append(i)
    return blist

alist = [1,2,3]
ans = f(alist)
print (ans)
print (alist) # alist has not been changed!
