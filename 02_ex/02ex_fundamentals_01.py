def f(m, A_list): #define a function
    local_list = A_list.copy()
    for i in range(m):
        local_list.append(i)
    return local_list #return statement


x = 5
alist = [1, 2, 3]
ans = f(x, alist)#we use from defined function
print(ans)
print(alist)  # alist is not changed anymore