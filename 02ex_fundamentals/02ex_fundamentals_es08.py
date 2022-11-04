def recur_f(n):
   if n <= 1:
       return n
   else:
       return(recur_f(n-1) + recur_f(n-2))

nterms = 20


print("First 20 numbers of the Fibonacci sequence:")
for i in range(nterms):
    print(recur_f(i))