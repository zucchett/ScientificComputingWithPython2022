#Q1 
x = 5
def f(alist):
    for i in range(x):
         alist.append(i)
    return alist

alist = [1,2,3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed!

#solution 
x=5
def f(alist):
    x=5  # value de
    alist=[1,2,3]
    for i in range(x):
        alist.append(i)
    return alist

alist=[1,2,3]
ans=f(alist)
print(ans)
print(alist)