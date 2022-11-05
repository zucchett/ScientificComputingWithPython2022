x = 5

def f(alist):
    temp_list = list(alist)
    for i in range(x):
         temp_list.append(i)
    return temp_list

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) 