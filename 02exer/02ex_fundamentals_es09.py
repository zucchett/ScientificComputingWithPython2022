#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import timeit
#for loop method
setup_code = """
Number = 20 #it is the number of elements in the sequence
i = 0 #it is the variable that iterates
First_Value = 0
Second_Value = 1
"""
main_code = """           
while(i < Number):
    if(i <= 1):
        Next = i
       
    else:
        Next = First_Value + Second_Value
        First_Value = Second_Value
        Second_Value = Next
    print("The element ",i+1,"of Fibonacci sequence is ",Next  )
    i +=  1
""" 

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

N = int(input("Maximum element of Fibonacci sequence: "))
for i in range(N):
    print(fibo(i))
    i += 1

tempo_rec = timeit.timeit('fibo(20)', globals=globals(), number=1)
tempo_loop = timeit.timeit(stmt=main_code,
          setup=setup_code,
          number=1)
print("Time of execution of fibonacci while loop is: ",tempo_loop)
print("Time for fibonacci recursive method is: ", tempo_rec)
#print(timeit.timeit(stmt=s),globals=globals(),number =1)
if tempo_loop < tempo_rec:
    print("The while loop is most efficient")
else:
    print("The recursive method is more efficient")