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
    
print(rec_fibo(20))