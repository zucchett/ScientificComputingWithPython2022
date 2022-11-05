def f(j, arg_list):
    local_list = arg_list.copy()
    for i in range(j):
        local_list.append(i)
    return local_list


x = 5
alist = [1, 2, 3]
ans = f(x, alist)
print(ans)
print(alist)  # alist is not changed anymore
