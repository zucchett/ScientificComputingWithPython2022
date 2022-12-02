# ex_09

from timeit import timeit

def loopFib(x): #loop from first set of exercises as function
    fibonacci = [1]
    f0 = 0
    f1 = f0 +1
    for i in range(x):
            fib = f0+f1
            fibonacci.append(fib)
            f0 = f1
            f1 = fib 
    return fibonacci

loop_time = timeit(stmt = 'loopFib(20)', setup = '', number = 1, globals=globals())
print("Using the loop function the employed time is: ", loop_time)

def Fib(x):
    if x==1 or x==0:
        return 1
    else:
        return Fib(x-2) + Fib(x-1)

recursive_time = timeit(stmt = 'Fib(20)', setup = 'fib = []', number = 1, globals=globals())

print("Using the recursive function the employed time is: ", recursive_time)   
print("The time difference between loop and recursive is: ", loop_time - recursive_time) 

