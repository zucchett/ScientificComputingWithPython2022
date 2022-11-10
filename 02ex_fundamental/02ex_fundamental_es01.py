def f(j, arg_list):
    a_list = list(arg_list)
    for i in range(j):
        a_list.append(i)
    return a_list


x = 5
alist = [1, 2, 3]
ans = f(x, alist)
print(ans)
print(alist)  