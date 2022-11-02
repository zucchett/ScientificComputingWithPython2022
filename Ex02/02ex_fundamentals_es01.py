#1. Global Variables

x = 5

def f(alist):
    alist = [item for item in alist] # reassigning the list to create a copy
    x = 5 # using local x instead of global variable
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)

print(ans)
print(alist) # alist has not been changed