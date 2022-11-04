'''
Fibonacci sequence using for loop
'''
import timeit
fib= [0, 1]
def loopFibonacci(n):
    for i in range(2, n):
        fib.append(fib[i-1]+fib[i-2])
        
        

start = timeit.default_timer()
loopFibonacci(20)
exe_time = timeit.default_timer() - start
print("Fibonacci sequence using for loop execution time  :", exe_time)


'''
recurcive function is way more time consuming than a for loop. the reason is by calling recursive function,  function should be called n-1 and n-2 times inside the function; in total 2n-3 operation. But in the for loop it goes from 0 to n-1. 
'''

