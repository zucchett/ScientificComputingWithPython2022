import timeit
fibo_list = [0,1,1]
def fiboloop():
    for i in range (3,19):
        next_fibo_value = fibo_list[i-2] + fibo_list[i-1]
        fibo_list.append(next_fibo_value)
#-----------------------------------------------------------------------------
recur_fibo_list = []
def recur_fibo_func() :
    def recur_fibo(n):
        if n <= 1:
            return n
        else:
            return(recur_fibo(n-1) + recur_fibo(n-2))
    for i in range(19):
        recur_fibo_list.append(recur_fibo(i))
#---------------------------------------------------------------------------------
time_1 = timeit.Timer(lambda:fiboloop())
time_2 = timeit.Timer(lambda:recur_fibo_func())
print(f'the proceed time for first solution is : {time_1.timeit(1)}')
print(f'the proceed time for second solution is : {time_2.timeit(1)}')