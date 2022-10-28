# 9. The Fibonacci sequence (part 3)

# Run both the Fibonacci recursive function
# from the previous exercise, and the Fibonacci
# function from 01ex that use only for and while loops.

# Measure the execution code of the two functions with
# timeit (link to the doc), for example:

# %timeit loopFibonacci(20)

# %timeit recursiveFibonacci(20)

# which one is the most efficient implementation? By how much?

import timeit

f = [1, 1]

# RECURSIVE FIBONACCI
def recursiveFibonacci(n):
    if n==0 or n==1:
        return n
    elif n==2:
        entry = recursiveFibonacci(n-1) + recursiveFibonacci(n-2)
        return entry
    else:
        entry = recursiveFibonacci(n-1) + recursiveFibonacci(n-2)
        if entry not in f:
            f.append(entry)
        return entry

recursiveFibonacci(20)

# LOOP FIBONACCI

def loopFibonacci(N):
    seq = []
    fibonacci = 0
    for i in range(N+1) :
        if i == 0 or i == 1:
            fibonacci = i
            seq.append(fibonacci)
        else :
            fibonacci = int(seq[i-1]) + int(seq[i-2])
            seq.append(fibonacci)
    return seq

loopTime = timeit.timeit(stmt='loopFibonacci(20)', globals=globals(), number=1000)/1000
recursiveTime = timeit.timeit(stmt='recursiveFibonacci(20)', globals=globals(), number=1000)/1000

if loopTime < recursiveTime:
    efficientTime = "loop algorithm"
else:
    efficientTime = "recursive algorithm"


print("The time required to execute the loopFibonacci(20) is: " + str(loopTime))
print("The time required to execute the recursiveFibonacci(20) is: " + str(recursiveTime))

print("The most efficient is the " + efficientTime)
print("The ratio between the two execution times is " + str(recursiveTime/loopTime))
