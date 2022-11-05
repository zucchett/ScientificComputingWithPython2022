#9. The Fibonacci sequence (part 3)
import timeit

def fibo1(n):
    if n<=1:
        return n
    else:
        return fibo1(n-2) + fibo1(n-1)
    
def recursiveFibonacci(t):
    print(list(map(fibo1,range(t))))


def loopFibonacci(n):
    a=[]
    i=0
    while i <n:
        if i <=1:
            a.append(i)
        else:
            a.append(a[i-1]+a[i-2])
        i+=1
    print(a)

starttime = timeit.default_timer()
loopFibonacci(20)
print("The loopFibonacci time is :", timeit.default_timer() - starttime)

starttime2 = timeit.default_timer()
recursiveFibonacci(20)
print("The recursiveFibonacci time is :", timeit.default_timer() - starttime2)

#which one is the most efficient implementation? By how much?
#The recursiveFibonacci is much more efficient by approximately 1500 time rapid execution!