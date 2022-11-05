''' Created by Pedram on 10/26/2022 AD. '''

def f(alist):
    for i in range(5):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f([1, 2, 3])
print(ans)
print(alist)

# OR

def f(alist):
    for i in range(5):
        alist.append(i)
    return alist

alist = [1, 2, 3]
a = [1, 2, 3]
ans = f(a)
print(ans)
print(alist)