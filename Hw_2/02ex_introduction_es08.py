def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

y=[]
for i in range(20):
    y.append(fibonacci(i))
print(y)