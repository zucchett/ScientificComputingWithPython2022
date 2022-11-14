from timeit import timeit

def Fibonacci(x): 
    fibo = [1]
    fib0 = 0
    fib1 = fib0 +1
    for i in range(x):
            fib = fib0+fib1
            fibo.append(fib)
            fib0 = fib1
            fib1 = fib 
    return fibo

LoopTime = timeit(stmt = 'Fibonacci(20)', setup = '', number = 1, globals=globals())
print("by using the loop function, employed time : ", LoopTime)

def Fib(x):
    if x==1 or x==0:
        return 1
    else:
        return Fib(x-2) + Fib(x-1)

RecursiveTime = timeit(stmt = 'Fib(20)', setup = 'fib = []', number = 1, globals=globals())

print("by using the recursive function,  employed time: ", RecursiveTime)   
print("time difference between the loop and the recursive: ", LoopTime - RecursiveTime) 