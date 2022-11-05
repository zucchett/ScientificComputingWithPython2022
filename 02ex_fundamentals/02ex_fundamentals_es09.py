#Loop Fibo
def loop_fibo (n):
    f_list = []
    for i in range(n):
        if (len(f_list) < 2):
            f_list.append(i)
        else:
            f_list.append(f_list[i-1] + f_list[i-2])
    return f_list

#Recursive Fibo
def rec_fibo(n):
    f_list = []
    def fibo(n):
        if (n <= 2):
            r = n-1
        else:
            r = fibo(n-2)+fibo(n-1)
        if (len(f_list) == n-1):
            f_list.append(r)
        return r
    fibo(n)
    return f_list

print("execution time using loops :")
%timeit loop_fibo(20)
print("execution time using recursive funstion :")
%timeit rec_fibo(20)