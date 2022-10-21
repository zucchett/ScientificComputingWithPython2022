x = 5

def f(a,x):
    alist = [i for i in a] 
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist,x)
print(ans)
print(alist)