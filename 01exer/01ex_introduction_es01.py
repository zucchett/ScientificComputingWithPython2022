#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import math 
i = 1
t = ()
while i < 101:
    if i%3==0 and i%15!=0:
        print("Hello")
        t += ("Python",)
        
    elif i%5==0 and i%15!=0:
        print("World")
        t += ("Works",)
   
    elif i%15==0:
        print("HelloWorld")
        t += ("PythonWorks",)
    else:
        print(i)
        t += (i,)
    i += 1
print()
print("Let's see the components of the tuple")
print(t)









