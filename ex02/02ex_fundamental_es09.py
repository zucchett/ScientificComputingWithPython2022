import timeit

def fibo_loop():
    srm, Sh1 , Sh2 , list_1 = 0 , 0 , 1 , []
    while srm <= 20:
        ABC = Sh1 + Sh2
        Sh1 = Sh2
        Sh2 = ABC
        srm += 1
        list_1.append(Sh1)
    print(list_1)

def fibo(n):
    if n < 2:
        return 1
    return fibo(n-1) + fibo(n-2)

time_1 = timeit.Timer(lambda: fibo_loop())
time_2 = timeit.Timer(lambda: [fibo(i) for i in range(20)])

time1 = time_1.timeit(1)
time2 = time_2.timeit(1)

print("Execution time of fibo calculation using loop: ", time1)
print("Execution time of fibo calculation using recursion: ", time2)

print("The difference between the execution times of loop function and recursion function is: ", time1 - time2)
# Using loop is much faster than recursion.