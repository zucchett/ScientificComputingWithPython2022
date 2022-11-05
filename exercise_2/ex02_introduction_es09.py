import timeit
# calculating fibonacci sequence from exercise one
def ex_01_fibonacci_sequence(n):
    f1 = 0
    f2 = 1
    fiboList = [0, 1]
    for x in range(2, n):
        fn = fiboList[x - 1] + fiboList[x - 2]
        fiboList.append(fn)
    return fiboList


# calculating fibonacci sequence from exercise two
def fibonacci_sequence(i, fibo_list=None):
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


t_ex_01 = timeit.Timer(lambda: ex_01_fibonacci_sequence(20))
t_ex_02 = timeit.Timer(lambda: fibonacci_sequence(20))
executionTimeOfForLoop = t_ex_01.timeit(1)
executionTimeOfRecursion = t_ex_02.timeit(1)
print("execution time of exercise one model: ", executionTimeOfForLoop)
print("execution time of exercise two model: ", executionTimeOfRecursion)
print("The execution of the loop implementation is faster by %2f" %
      (executionTimeOfRecursion - executionTimeOfForLoop), " seconds.",
      "Therefore it's more efficient")
