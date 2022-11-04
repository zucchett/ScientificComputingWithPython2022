def fibo(n):
   if n == 0 :
      return 0
   elif n == 1:
      return 1
   else:
      return(fibo(n-1) + fibo(n-2))
x=[]
n=20
for i in range(n):
    x.append(fibo(i))


def Fibonacci(length):
    a = 0
    b = 1
    length -= 2
    x = [0,1]
    while length > 0:

        temp = b
        b += a
        x.append(b)
        a = temp

        length -= 1
    return(x)

Fibonacci(20)


%timeit fibo(20)

%timeit Fibonacci(20)