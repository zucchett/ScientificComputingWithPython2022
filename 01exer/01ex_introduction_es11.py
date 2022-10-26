#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import time
t1=time.time()
Number = 20 #it is the number of elements in the sequence
i = 0 #it is the variable that iterates
First_Value = 0
Second_Value = 1
           

while(i < Number):
    if(i <= 1):
        Next = i
       
    else:
        Next = First_Value + Second_Value
        First_Value = Second_Value
        Second_Value = Next
    print("The element ",i+1,"of Fibonacci sequence is ",Next  )
    i +=  1
t2=time.time()
print(t2-t1)
