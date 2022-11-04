# 9. fibonacci part 3

import timeit


def loopFibonacci(n):
    fibonacci = []
    for i in range(0,20):
        if(i == 0):
            fibonacci.append(0)
        elif(i == 1):
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    return fibonacci

def recursiceFibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return recursiceFibonacci(n-1) + recursiceFibonacci(n-2)

fibSequence = [recursiceFibonacci(x) for x in range(20)]

loopTime = timeit.Timer(lambda: loopFibonacci(20)).timeit(1)
recursiveTime = timeit.Timer('fibSequence', setup='from __main__ import fibSequence').timeit(1)

print(loopTime)
print(recursiveTime)
print("Difference in time:", loopTime-recursiveTime)

# The recurscive method is faster than the iterative approach almost by 7-9 microsec.