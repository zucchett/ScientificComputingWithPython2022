
# 9. The Fibonacci sequence (part 3)

# Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only for and while loops.

# Measure the execution code of the two functions with timeit (link to the doc), for example:

# %timeit loopFibonacci(20)

# %timeit recursiveFibonacci(20)

# which one is the most efficient implementation? By how much?

# -------------------------------------- Code Begin-------------------------------------

import timeit
def recursiveFibonacci(n):
    if n == 0 :
        return 0
    elif n==1 or n==2:
        return 1
    else :
        return recursiveFibonacci(n-1) +  recursiveFibonacci(n-2)

def loopFibonacci(n):
    fib = []
    for i in range(n): 
        if i==0:
            fib.append(0)
        elif i==1:
            fib.append(1)
        else:
            fib.append(fib[-1] + fib[-2])

print('-----------recursiveFibonacci-------')
        
starttime = timeit.default_timer()
print("The start time recursiveFibonacci is :",starttime)
recursiveFibonacci(20)
print("The time difference for recursiveFibonacci is :", timeit.default_timer() - starttime)

print('-----------loopFibonacci-------')
starttime = timeit.default_timer()
print("The start time loopFibonacci is :",starttime)
loopFibonacci(20)
print("The time difference for loopFibonacci is :", timeit.default_timer() - starttime)


# -------------------------------------- Code End -------------------------------------
