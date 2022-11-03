#1.Global variables

#Initial code
x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed


#Modified code  without global variables
def f(alist,x=5):
    l=alist.copy()
    for i in range(x):
        l.append(i)
    return l
alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist doesn't change
