#8. The Fibonacci sequence (part 2)

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibSequence = [fibonacci(x) for x in range(20)]

print(fibSequence)