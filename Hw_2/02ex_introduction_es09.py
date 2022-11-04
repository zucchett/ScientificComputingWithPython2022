import timeit

def fibonacci(n):
    if n <= 1:
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
 

def loopFibonacci(n):
    f=[]
    for i in range (n):
        f.append(i)
        if i>1:
            f[i]= f[i-1]+f[i-2]

def recursiveFibonacci(n):
    y=[]
    for i in range(n):
        y.append(fibonacci(i)) 
    return y 


starttime=timeit.default_timer()
loopFibonacci(20)
endtime=timeit.default_timer()
print("Timer for Fibonacci: ",(endtime-starttime))

starttime1=timeit.default_timer()
recursiveFibonacci(20)
endtime1=timeit.default_timer()
print("Timer for recursiveFibonacci: ",(endtime1-starttime1))

