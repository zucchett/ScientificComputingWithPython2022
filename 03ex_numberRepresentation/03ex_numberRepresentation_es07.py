import math
import timeit

n = 500000
def f(n):
    result = 0
    for x in range(0,n):
        result = result + math.sqrt(1-pow((x/n),2))
    return (result*2/n)
print(f"The Result of a is : {f(n)}")

"""For section a the result is changes after third number.
when i increased the number of N it become more accurate.
"""

n = 990000
def f(n):
    result = 0
    for x in range(0,n):
        result = result + math.sqrt(1-pow((x/n),2))
    return (result*2/n)

print(f"The result of the b is : {f(n)}")
print(timeit.timeit("f(960000)",setup="from __main__ import f",number=1))  #between 955000(0.9835665999999175 seconds) and 960000(1.065322800002014 seconds) loops it computes under a second 
print(timeit.timeit("f(55500000)",setup="from __main__ import f",number=1))  #if we give N=55500000, it takes 40.080835300002946 seconds to compute