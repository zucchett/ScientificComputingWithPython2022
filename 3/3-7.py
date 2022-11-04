##################    A    ##################### 
import math
from math import sqrt
import timeit

true_Value = math.pi / 2
print(" True value: ", true_Value)

def integral_fun(under, upper, c):
    Ans = 0
    m = (upper - under) / c

    for i in range(0, c - 1):
        current_x = under + i * m
        Ans += sqrt(1 - current_x ** 2) * m

    print("integral value : ", Ans)
    print(" difference : ", true_Value - Ans)
    return Ans
integral = integral_fun(-1, 1, 100)


##############################   B   ################################

def run_code_for_seconds(sec, k):
    Ans = 0
    exec_time = 0
    n = 10000
    while exec_time <= sec:
        n += k
        start_time = timeit.default_timer()
        Ans = integral_fun(-1, 1, n)
        end_time = timeit.default_timer()
        exec_time = end_time - start_time
        print("running with n: ", n, "and exec time:", exec_time)

    print("Result: ", Ans)
    print("execution time: ", exec_time, " seconds.")
    print("The N has gone to: ", n)
print("for 1 sec:")

# For N = 4000000 execution time is 1 second.
N = 4000000
intTime = timeit.Timer(lambda: integral_fun(-1, 1, N))
print("Execution time for N =4000000 is: ", intTime.timeit(1))


print("Running function for 60 sec:")

# for approximately N=2.4e8 the integral function will run for 1 minutes.

N = 240000000
intTime = timeit.Timer(lambda: integral_fun(-1, 1, N))
print("Execution time for N = 240000000  is: ", intTime.timeit(1))