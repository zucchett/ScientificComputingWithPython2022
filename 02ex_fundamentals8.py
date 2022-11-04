fib=[0,1]
def fibonacci(n,i):
  if i <n:
    fib.append(fib[i-2]+fib[i-1])
    fibonacci(n,i+1)
  else:
    print(fib)
fibonacci(20,2)
print(len(fib))
