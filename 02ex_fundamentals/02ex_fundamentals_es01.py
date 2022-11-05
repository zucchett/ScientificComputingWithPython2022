x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed

#My optimized code

x = 5
alist_temp =[]

def f(alist):
    alist_temp = alist
    for i in range(x):
         alist_temp.append(i)
    return alist_temp

alist = [1,2,3]
ans = f(alist)

print(ans)
print(alist) 