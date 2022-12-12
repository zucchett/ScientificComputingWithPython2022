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
x
