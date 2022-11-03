import timeit
def ex_01_fibonacci_sequence(n):# calculating fibonacci sequence(exe1)
    f1 = 0
    f2 = 1
    fiboList = [0, 1]
    for i in range(2, n):
        fn = fiboList[i - 1] + fiboList[i - 2]
        fiboList.append(fn)
    return fiboList

def fibonacci_sequence(i, fibo_list=None):# calculating fibonacci sequence(exe2)
    if fibo_list is None:
        fibo_list = []
    if i == 0:
        return fibo_list
    if len(fibo_list) == 0:
        fibo_list.append(0)
    elif len(fibo_list) == 1:
        fibo_list.append(1)
    else:
        fibo_list.append(fibo_list[-2] + fibo_list[-1])
    fibonacci_sequence(i - 1, fibo_list)
    return fibo_list


time_ex_01 = timeit.Timer(lambda: ex_01_fibonacci_sequence(20))
time_ex_02 = timeit.Timer(lambda: fibonacci_sequence(20))
executionTime_ForLoop = time_ex_01.timeit(1)
executionTime_Recursion = time_ex_02.timeit(1)
print("execution time of e1: ", executionTime_ForLoop)
print("execution time of e2: ", executionTime_Recursion)
print("The  loop implementation is faster by %2f" %
      (executionTime_Recursion - executionTime_ForLoop), " seconds.",)