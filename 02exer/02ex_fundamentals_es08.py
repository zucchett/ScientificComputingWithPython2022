#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import time
t1=time.time()
#define function
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
N = int(input("Maximum element of Fibonacci sequence: "))
#print values
for i in range(N):
    print(fibo(i))
    i += 1

t2 = time.time()
print(t2-t1)