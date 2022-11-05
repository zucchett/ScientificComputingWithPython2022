# Python program to display the Fibonacci sequence
recur_fibo_list = []
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

for i in range(19):
    recur_fibo_list.append(recur_fibo(i))
print(recur_fibo_list)