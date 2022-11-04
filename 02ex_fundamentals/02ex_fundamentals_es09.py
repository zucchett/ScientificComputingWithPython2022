from timeit import timeit

def loopFib(x): 
    fibonacci = [1]
    n1 = 0
    n2 = n1 +1
    for i in range(x):
            fib = n1+n2
            fibonacci.append(fib)
            n1 = n2
            n2 = fib 
    return fibonacci

loop_time = timeit(stmt = 'loopFib(20)', setup = '', number = 1, globals=globals())
print("Using the loop function the employed time is: ", loop_time)

def recursiveFib(x):
    if x==1 or x==0:
        return 1
    else:
        return recursiveFib(x-2) + recursiveFib(x-1)
    
recursive_time = timeit(stmt = 'recursiveFib(20)', setup = 'fib = []', number = 1, globals=globals())
print("Using the recursive function the employed time is: ", recursive_time)   
print("The time difference between loop and recursive is: ", loop_time - recursive_time) 
print()
