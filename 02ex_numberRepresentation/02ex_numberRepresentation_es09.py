def recursiveFibonacci(n):
   if n <= 1:
       return n
   else:
       return(recursiveFibonacci(n-1) + recursiveFibonacci(n-2))

def loopFibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

print("Loop Fibonacci Time: ")
%timeit loopFibonacci(20)

print("Recursive Fibonacci Time: ")
%timeit [recursiveFibonacci(n) for n in range(20)]
