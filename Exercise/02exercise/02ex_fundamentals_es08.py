#8. The Fibonacci sequence (part 2)
def fibo1(n):
    if n<=1:
        return n
    else:
        return fibo1(n-2) + fibo1(n-1)
    
count=20
print(list(map(fibo1,range(count))))

