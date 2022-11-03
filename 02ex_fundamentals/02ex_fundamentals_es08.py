#8. The Fibonacci sequence (part 2)

def Fibonacci(n):
    if n==0: 
        return 0
    elif n==1: 
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
for i in range(20):
    print('F%d = %d' %(i, Fibonacci(i)))
