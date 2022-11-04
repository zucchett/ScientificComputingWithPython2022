def recursiveFibonacci(n):
   if n <= 1:
       return n
   else:
       return(recursiveFibonacci(n-1) + recursiveFibonacci(n-2))
       
[recursiveFibonacci(n) for n in range(20)]