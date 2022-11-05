# The Fibonacci sequence (part 3)

import timeit

def loopFibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(0, n):
            if(i == 0):
                fibonacci_list.append(a)
            elif(i == 1):
                fibonacci_list.append(b)
            else:
                c = a + b
                a = b
                b = c
                fibonacci_list.append(c)

fibonacci_list=[]
loopFibonacci(20)
print(fibonacci_list)


def recursiveFibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return recursiveFibonacci(n-1)+recursiveFibonacci(n-2)

fibonacci_list=[]
for i in range(0,20):
    fibonacci_list.append(recursiveFibonacci(i))

print(fibonacci_list)

resultLoop = timeit.timeit(stmt='loopFibonacci(20)', globals=globals(), number=1)
resultRec = timeit.timeit(stmt='recursiveFibonacci(20)', globals=globals(), number=1)

print("Time to computer loop algorithm: "+str(resultLoop))
print("Time to computer recursive algorithm: "+str(resultRec))
print("Differences of the two results: "+str(abs(resultLoop - resultRec)))

# The iterative algorithm works better, this is because the recursive procedure must be performed 
# for smaller instances each time the recursiveFibonacci(n) function is called.
# This requires more and more computational effort as n increases.