import math
from math import sqrt
import timeit


trueValue = math.pi / 2
print("The True value is: ", trueValue)

def integral_fun(start, end, count):
    result = 0
    h = (end - start) / count

    for i in range(0, count - 1):
        current_x = start + i * h
        result += sqrt(1 - current_x ** 2) * h

    print("The value of integral is: ", result)
    print("The difference of integral and true value is : ", trueValue - result)
    return result


integral = integral_fun(-1, 1, 100)

# Part B

def run_code_for_seconds(sec, steps):
    result = 0
    exec_time = 0
    n = 10000
    while exec_time <= sec:
        n += steps
        start_time = timeit.default_timer()
        result = integral_fun(-1, 1, n)
        end_time = timeit.default_timer()
        exec_time = end_time - start_time
        print("running with n: ", n, "and exec time:", exec_time)

    print("Result: ", result)
    print("Execution time: ", exec_time, " seconds.")
    print("The N has gone to: ", n)

print("Running function for 1 sec:")
# run_code_for_seconds(1, 100000) #this statement will find N-for 1 second of running integral fun
# For N = 4.0e6 the execution time of the integral function will be around 1 second.
# Testing the execution time of the function with timeit:
N = 4000000
intTime = timeit.Timer(lambda: integral_fun(-1, 1, N))
print("Execution time of Integral function with N =",N, " is: ", intTime.timeit(1))
print("---------End----------")


print("Running function for 60 sec:")
# run_code_for_seconds(60, 10**7) #this statement will find N-for 60 second of running integral fun
# Ran the timing function to find the value of N for running in 60 seconds.
# The result was:
# for approximately N=2.4e8 the integral function will run for 1 minutes.
# The result of integral in this case is much closer to the real value.
N = 240000000
intTime = timeit.Timer(lambda: integral_fun(-1, 1, N))
print("Execution time of Integral function with N =",N, " is: ", intTime.timeit(1))
print("---------End----------")
