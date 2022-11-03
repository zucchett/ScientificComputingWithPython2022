# The Fibonacci sequence (part 2)

def recursiveFibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return recursiveFibonacci(n-1)+recursiveFibonacci(n-2)

fibonacci_list=[]
for i in range(0,20):
    fibonacci_list.append(recursiveFibonacci(i))

print(fibonacci_list)