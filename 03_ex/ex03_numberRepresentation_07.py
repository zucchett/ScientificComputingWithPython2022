import math# Part A
from math import sqrt
import timeit

tr_Value = math.pi / 2
print(" True value: ", tr_Value)

def integral_fun(start, end, count):
    Answer = 0
    m = (end - start) / count

    for i in range(0, count - 1):
        current_x = start + i * m
        Answer += sqrt(1 - current_x ** 2) * m

    print("The integral value : ", Answer)
    print(" integral and true difference : ", tr_Value - Answer)
    return Answer
integral = integral_fun(-1, 1, 100)#end of part a

def run_code_for_seconds(sec, step):# Part B
    Answer = 0
    exec_time = 0
    n = 10000
    while exec_time <= sec:
        n += step
        start_time = timeit.default_timer()
        Answer = integral_fun(-1, 1, n)
        end_time = timeit.default_timer()
        exec_time = end_time - start_time
        print("running with n: ", n, "and exec time:", exec_time)

    print("Result: ", Answer)
    print("execution time: ", exec_time, " seconds.")
    print("The N has gone to: ", n)
print("Running function for 1 sec:")

# #this statement will find N-for 1 second of running integral fun
# For N = 4000000 the execution time of the integral function will be around 1 second.
N = 4000000
intTime = timeit.Timer(lambda: integral_fun(-1, 1, N))
print("Execution time of Integral function with N =",N, " is: ", intTime.timeit(1))
print("---------wait 60 sec for running function ----------")


N = 240000000
intTime = timeit.Timer(lambda: integral_fun(-1, 1, N))
print("Execution time of Integral function with N =",N, " is: ", intTime.timeit(1))
print("---------End----------")

# Ran the timing function to find the value of N for running in 60 seconds.
# for  N=2.4e8 the integral function will run for 60 seconds.
# integral result  is much closer to the real value.