import timeit
def recursive_Fib(n):
   if n <= 1:
       return n
   else:
       return(recursive_Fib(n-1) + recursive_Fib(n-2))

n =int(input ("enter number to calculacted recursive fibunacci!"))

# check if the number of terms is valid
if n <= 0:
   print("Plese enter a positive number")
else:
   print("Fibonacci sequence :")
   for i in range(n):
       print(recursive_Fib(i))   
print("time for recursive Fibunacci is  ")
%timeit recursive_Fib(n)

code="""
def loopFibonacci(n):
    i = 1
    num1, num2=0,1
    while(i<=n):
        
        print(num1)
        next=num1+num2
        
        num1=num2
        num2=next
        i+=1
"""

print("time for loop fibunacci is  ",timeit.timeit(stmt=code, number=1000000))