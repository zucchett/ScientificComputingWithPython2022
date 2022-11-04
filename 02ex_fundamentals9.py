import timeit

starttime = timeit.default_timer()
fib=[0,1]
def loop_fibonacci(n):
    for i in range(n-2):
        fib.append(fib[i] + fib[i+1])
print("_____________________________________________________________________________________\n")
print("The start time for loop_fibonacci function is :",starttime)
loop_fibonacci(20)
print(fib)
print("The time difference is :", timeit.default_timer() - starttime)
print("_____________________________________________________________________________________\n")
starttime = timeit.default_timer()
fib=[0,1]
def recrusive_fibonacci(n,i):
   if i <n:
    fib.append(fib[i-2]+fib[i-1])
    recrusive_fibonacci(n,i+1)
   else:
    print(fib)   
print("The start time for recursive_fibonacci function is :",starttime)
recrusive_fibonacci(20,2)
print("The time difference is :", timeit.default_timer() - starttime)
print("_____________________________________________________________________________________\n")