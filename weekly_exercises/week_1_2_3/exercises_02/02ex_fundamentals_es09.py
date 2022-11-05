#Zuccolo Giada, matr. 2055702
# EXE 9

import timeit

def loopFibonacci(r):
    n1 = 0
    n2 = n1 + 1
    fib = []
    for x in range(r):
        #print(n1)
        fib.append(n1)
        tmp = n1 + n2
        n1 = n2
        n2 = tmp
    return fib

def fibonacci_recursive(r):
    def fibonacci_sequence(n):
        if n <= 1:
            return n
        else:
            return (fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2))
    fib=[]
    for i in range(r):
        fib.append(fibonacci_sequence(i))
    return fib

r = 5
#print(loopFibonacci(r))
#print(fibonacci_recursive(r))
time_loop = timeit.timeit("loopFibonacci(r)", globals=globals())
time_recursive = timeit.timeit("fibonacci_recursive(r)", globals=globals())
print("TIME\nLoop Fibonacci: \t" + str(time_loop) +"\nRecursive Fibonacci: \t" + str(time_recursive))
max = lambda x, y: x > y
if (max(time_loop, time_recursive)):
    print("Recursive Fibonacci is faster than Loop Fibonacci by "+str(time_loop - time_recursive)+" seconds")
else:
    print("Loop Fibonacci is faster than Recursive Fibonacci by "+str(time_recursive - time_loop)+" seconds")
