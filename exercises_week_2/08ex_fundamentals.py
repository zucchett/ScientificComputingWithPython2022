#8. The Fibonacci sequence (part 2)
 
def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

f_sequence =[]
for i in (range(5)):
    f_sequence.append(fibonacci(i))

print(f_sequence)